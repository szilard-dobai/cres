import json
import random

from gui import *

candidates = []


def init():
    with open('KB.json') as KB_file:
        kb = json.load(KB_file)
    for entry in kb['KB']:
        e = dict()
        e['car'] = entry['car']
        e['rules'] = dict()
        for rule in entry['rules'].keys():
            e['rules'][rule] = {"value": entry["rules"][rule], "flag": False}
        candidates.append(e)

    with open('AppStrings.json') as app_strings_file:
        app_strings = json.load(app_strings_file)
    for entry in app_strings['qa']:
        q = dict()
        q['text'] = entry['question']['text']
        q['answers'] = []
        for ans in entry['answers']:
            answers[ans['id']] = ans['text']
            q['answers'].append(ans['id'])
        questions[entry['question']['id']] = q


def run_iteration():
    global inpQ, inpA, candidates

    interm = []
    for entry in candidates:
        if inpQ in entry['rules'].keys() and entry['rules'][inpQ]['value'] == inpA:
            entry['rules'][inpQ]['flag'] = True
            overall_flag = True
            for predicate in entry['rules'].keys():
                overall_flag = overall_flag and entry['rules'][predicate]['flag']
            if overall_flag:
                results.append(entry)
            else:
                interm.append(entry)

    if interm.__len__() == 0:
        return False

    random_index = random.randint(0, interm.__len__() - 1)
    for predicate in interm[random_index]['rules'].keys():
        if not interm[random_index]['rules'][predicate]['flag']:
            inpQ = predicate
            break
    candidates = interm
    return True


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):

        tk.Frame.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        button_frame = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        button_frame.pack(side="bottom", fill="x", expand=False, pady=15, padx=15)

        welcome_page = WelcomePage(self)
        welcome_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        form_pages = []

        current_page = "welcome_page"
        button_text = tk.StringVar()
        button_text.set("Begin")

        def validate(self, *args):
            if answer_var.get() != '':
                button['state'] = 'normal'

        answer_var.trace('w', validate)

        def button_click():
            global inpQ, inpA
            nonlocal current_page
            if current_page == "welcome_page":
                inpQ = "why"
                question_label_text.set(inpQ)
                answer_var.set("1")

                fp = FormPage(self)
                fp.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
                fp.show()
                form_pages.append(fp)

                button_text.set("Next")
                current_page = "form_page"
                button['state'] = 'disabled'
            elif current_page == "form_page":
                inpA = answer_var.get()
                print(answer_var.get())
                if run_iteration():
                    question_label_text.set(inpQ)
                    answer_var.set("1")

                    button['state'] = 'disabled'

                    fp = FormPage(self)
                    fp.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
                    fp.show()
                    form_pages.append(fp)
                else:
                    button_text.set("Exit")

                    current_page = "results_page"

                    results_page = ResultPage(self)
                    results_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
                    results_page.show()
            elif current_page == "results_page":
                root.quit()

        button = tk.Button(button_frame, textvariable=button_text, command=button_click)
        button.pack(side="bottom")

        welcome_page.show()


init()

main = MainView(root)
main.pack(side="top", fill="both", expand=True)

root.wm_title("Car Recommendation Expert System")
root.wm_geometry("400x800")
root.resizable(False, False)
root.mainloop()
