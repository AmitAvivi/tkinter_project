import tkinter as tk
from tkinter import ttk


class ResultsFrame(ttk.Frame):

    def __init__(self, parent, controller, show_search):
        super().__init__(parent)

        self.parent = parent
        self.controller = controller
        self.show_search = show_search
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        results_title_label = ttk.Label(
            self,
            text="Results",
            font=("Segoe UI", 20)
        )
        results_title_label.grid(row=0, column=0, columnspan=2)

        names_label = ttk.Label(
            self,
            text="Names :"
        )
        names_label.grid(row=1, column=0, sticky="NESW")

        names_text_box = ttk.Entry(
            self,
            width=80,
            textvariable=controller.names_text,
            state="disabled"
        )
        names_text_box.grid(row=1, column=1, sticky="NESW")



        titles_label = ttk.Label(
            self,
            text="Titles :"
        )
        titles_label.grid(row=2, column=0, sticky="NESW")

        title_text_box = ttk.Entry(
            self,
            width=80,
            textvariable=controller.titles_text,
            state="disabled"
        )
        title_text_box.grid(row=2, column=1, sticky="NESW")

        tv_episodes_label = ttk.Label(
            self,
            text="TV Episodes :"
        )
        tv_episodes_label.grid(row=3, column=0, sticky="NESW")

        tv_episodes_text_box = ttk.Entry(
            self,
            width=80,
            textvariable=controller.tv_episodes_text,
            state="disabled"
        )
        tv_episodes_text_box.grid(row=3, column=1, sticky="NESW")

        celebs_label = ttk.Label(
            self,
            text="Celebs :"
        )
        celebs_label.grid(row=4, column=0, sticky="NESW")

        celebs_text_box = ttk.Entry(
            self,
            width=80,
            textvariable=controller.celebs_text,
            state="disabled"
        )
        celebs_text_box.grid(row=4, column=1, sticky="NESW")

        companies_label = ttk.Label(
            self,
            text="Companies :"
        )
        companies_label.grid(row=5, column=0, sticky="NESW")

        companies_text_box = ttk.Entry(
            self,
            width=80,
            textvariable=controller.companies_text,
            state="disabled"
        )
        companies_text_box.grid(row=5, column=1, sticky="NESW")

        keywords_label = ttk.Label(
            self,
            text="Keywords :"
        )
        keywords_label.grid(row=6, column=0, sticky="NESW")

        keywords_text_box = ttk.Entry(
            self,
            width=80,
            textvariable=controller.keywords_text,
            state="disabled"
        )
        keywords_text_box.grid(row=6, column=1, sticky="NESW")

        return_button = ttk.Button(
            self,
            text="<- Back",
            command=self.delete_results,
            style="buttons.TButton",
            cursor="hand2"
        )
        return_button.grid(row=7, column=0, columnspan=2, sticky="NESW")

    def delete_results(self):
        sections = {"Names": self.controller.names_text,
                    "Titles": self.controller.titles_text,
                    "Keywords": self.controller.keywords_text,
                    "Companies": self.controller.companies_text,
                    "Celebs": self.controller.celebs_text,
                    "TV Episodes": self.controller.tv_episodes_text}
        for section in sections:
            sections[section].set("No Results Found!")
        self.show_search()









