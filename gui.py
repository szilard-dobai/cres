import tkinter as tk

# from main import *


root = tk.Tk()  # instantiate tkinter Tk class

questionLabel = tk.StringVar()  # create tkinter StringVar objects


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class WelcomePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label_title = tk.Label(self, text="Welcome to C.R.E.S.!", font=("Courier", 21))
        label_title.pack(side="top", expand=False, pady=[100, 0])

        label_description = tk.Label(self, text="Car Recommendation Expert System", font=("Courier", 12))
        label_description.pack(side="top", fill="x", expand=False, pady=[0, 100])

        label_begin = tk.Label(self, text="Click the button below to begin!")
        label_begin.pack(side="top", fill="x", expand=False)


class FormPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)


class ResultPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = WelcomePage(self)
        p2 = FormPage(self)
        p3 = ResultPage(self)

        current_page = "p1"
        button_text = tk.StringVar()

        button_text.set("Begin")

        button_frame = tk.Frame(self)
        container = tk.Frame(self)
        button_frame.pack(side="bottom", fill="x", expand=False, pady=15, padx=15)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        def button_click():
            nonlocal current_page
            if current_page == "p1":
                p2.lift()
                button_text.set("Next")
                current_page = "p2"

        button = tk.Button(button_frame, textvariable=button_text, command=button_click)

        button.pack(side="bottom")

        p1.show()