import tkinter as tk
from tkinter import ttk
import requests
import bs4


class SearchFrame(ttk.Frame):

    def __init__(self, parent, controller, show_results):
        super().__init__(parent)

        self.show_results = show_results
        self.controller = controller
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.title_label = ttk.Label(
            self,
            text="IMDB SEARCH ENGINE",
            font=("Segoe UI", 25),
            anchor="center",
            style="labelsText.TLabel"
        )
        self.title_label.grid(row=0, column=1, sticky="EW")


        search_label = ttk.Label(
            self,
            text="Search IMDB: "
        )
        search_label.grid(row=1, column=0, sticky="EW")

        self.search_text_box = ttk.Entry(
            self,
            width=30,
            textvariable=controller.search_word
        )
        self.search_text_box.grid(row=1, column=1, sticky="EW")
        self.search_text_box.focus()

        self.search_button = ttk.Button(
            self,
            text="Search!",
            command=self.get_search_results,
            style="buttons.TButton",
            cursor="hand2"
        )
        self.search_button.grid(row=1, column=2, sticky="EW")

        controller.bind("<Return>", self.search_button["command"])
        controller.bind("<KP_Enter>", self.search_button["command"])

    def get_results_data_text(self, search_word):
        payload = {'q': search_word, 'ref_': 'nv_sr_sm'}
        r = requests.get('https://www.imdb.com/find', params=payload)
        return r.text

    def extract_results(self, section):
        names = []
        trs = section.find_all("tr")
        for tr in trs:
            names.append(tr.text.strip())
        name_list = ""
        for name in names:
            if len(name_list) + len(name) + 2 < 80:
                name_list += name + ", "
        temp_list = list(name_list)
        temp_list[len(temp_list) - 2] = "."
        names = "".join(temp_list).strip()
        return names

    def get_search_results(self):
        if not self.controller.search_word.get():
            return
        search_word = self.controller.search_word.get()
        page_text = self.get_results_data_text(search_word)
        soup = bs4.BeautifulSoup(page_text, features="html.parser")
        sections = soup.find_all("div", "findSection")
        for section in sections:
            sectionName = section.find("h3").get_text()
            if sectionName == "Names":
                self.controller.names_text.set(self.extract_results(section))
            elif sectionName == "Titles":
                self.controller.titles_text.set(self.extract_results(section))
            elif sectionName == "TV Episodes":
                self.controller.tv_episodes_text.set(self.extract_results(section))
            elif sectionName == "Celebs":
                self.controller.celebs_text.set(self.extract_results(section))
            elif sectionName == "Companies":
                self.controller.companies_text.set(self.extract_results(section))
            elif sectionName == "Keywords":
                self.controller.keywords_text.set(self.extract_results(section))
        sections = {"Names": self.controller.names_text,
                    "Titles": self.controller.titles_text,
                    "Keywords": self.controller.keywords_text,
                    "Companies": self.controller.companies_text,
                    "Celebs": self.controller.celebs_text,
                    "TV Episodes": self.controller.tv_episodes_text}
        for section in sections:
            if not (sections[section].get()):
                sections[section].set("No ResultsFound!")
        self.search_text_box.delete(0, 'end')

        self.show_results()


