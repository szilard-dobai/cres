import tkinter as tk
from PIL import ImageTk, Image


def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


root = tk.Tk()  # instantiate tkinter Tk class

center_window(400, 800)

results = []
questions = dict()
answers = dict()
inpQ = ''
inpA = ''

question_label_text = tk.StringVar()  # create tkinter StringVar objects
answer_var = tk.StringVar()


class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        def _on_mouse_wheel(event):
            canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

        canvas.pack(side="left", fill="y")
        scrollbar.pack(side="right", fill="y")


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
        label_begin.pack(side="top", fill="x", expand=True)


class FormPage(Page):
    def __init__(self, *args, **kwargs):
        global inpQ, questions, answers
        Page.__init__(self, *args, **kwargs)
        label_title = tk.Label(self, text="C.R.E.S.", font=("Courier", 21))
        label_title.pack(side="top", expand=False, pady=[50, 0])

        label_description = tk.Label(self, text="Car Recommendation Expert System", font=("Courier", 12))
        label_description.pack(side="top", fill="x", expand=False, pady=[0, 50])

        question_label = tk.Label(self, text=questions[question_label_text.get()]['text'], wraplength=375)
        question_label.pack(side="top", fill="both", expand=True)

        print(question_label_text.get())
        for ans_id in questions[question_label_text.get()]['answers']:
            radio = tk.Radiobutton(self, text=answers[ans_id], value=ans_id, variable=answer_var, wraplength=375)
            radio.pack(side="top", ipady=5)


class ResultPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label_title = tk.Label(self, text="C.R.E.S.", font=("Courier", 21))
        label_title.pack(side="top", expand=False, pady=[50, 0])

        label_description = tk.Label(self, text="Car Recommendation Expert System", font=("Courier", 12))
        label_description.pack(side="top", fill="x", expand=False, pady=[0, 50])

        frame = ScrollableFrame(self)

        load = Image.open("parrot.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        if results.__len__() == 0:
            r_label = tk.Label(frame.scrollable_frame, text='Get a bike')
            r_label.pack(side="top", ipady=5)
        else:
            for res in results:
                r_label_name = tk.Label(frame.scrollable_frame, text=res['car']['name'])
                r_label_name.pack(side="top", ipady=5)

                r_label_description = tk.Label(frame.scrollable_frame, text=res['car']['description'], wraplength=375)
                r_label_description.pack(side="top", ipady=5)

        frame.pack(fill="both", expand=True)
