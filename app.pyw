import tkinter as tk
from tkinter import ttk
from tkinter_guide.windows_dpi import set_dpi_awareness
from imdb_app.frames.search_frame import SearchFrame
from imdb_app.frames.results_frame import ResultsFrame

set_dpi_awareness()

COLOUR_PRIMARY = "#2e3f3f"  # blue
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"

class IMDBSearchApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(
            "labelsText.TLabel",
            background=COLOUR_LIGHT_BACKGROUND,
            foreground=COLOUR_DARK_TEXT,
            font="Courier 38"
        )
        style.configure(
            "buttons.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT
        )

        style.map(
            "buttons.TButton",
            background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
        )
        self["background"] = COLOUR_PRIMARY


        self.title("IMDB Search App")
        self.geometry("600x400")
        self.resizable(False, False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.search_word = tk.StringVar()

        self.titles_text = tk.StringVar()
        self.tv_episodes_text = tk.StringVar()
        self.celebs_text = tk.StringVar()
        self.companies_text = tk.StringVar()
        self.keywords_text = tk.StringVar()
        self.names_text = tk.StringVar()

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = dict()

        search_frame = SearchFrame(container, self, lambda: self.show_frame(ResultsFrame))
        search_frame.grid(row=0, column=0, sticky="NESW")
        results_frame = ResultsFrame(container, self, lambda: self.show_frame(SearchFrame))
        results_frame.grid(row=0, column=0, sticky="NESW")

        self.frames[SearchFrame] = search_frame
        self.frames[ResultsFrame] = results_frame


        self.show_frame(SearchFrame)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


app = IMDBSearchApp()
app.mainloop()
