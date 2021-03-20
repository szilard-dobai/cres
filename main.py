import json
import random

from gui import *

candidates = []
results = []

window_background = "#F2F2F4"
text_color = "#2D2F57"


# root.config(background=window_background)                               # set background color


# frame = tk.Frame(root, width=1200, bg=window_background, pady=10)
# frame.grid(row=0)


def init():
    # step 1
    # init function
    #   read kb from file and initialize global candidates array
    with open('KB.json') as KB_file:
        kb = json.load(KB_file)
    for entry in kb['KB']:
        e = dict()
        e['car'] = entry['car']
        e['rules'] = dict()
        for rule in entry['rules'].keys():
            e['rules'][rule] = {"value": entry["rules"][rule], "flag": False}
        candidates.append(e)


# step 2
# get first input from user (why = transport / fun)
inpQ = 'why'
inpA = 'transport'


# step 3
# run algorithm
#   filter candidates array
#       check 'rules' object of each KB entry and if car.rules[obj].value === input, set car.rules[obj].flag = 1
#           if all flags are true, add car to results array, else continue looking for matches until no more candidates
#       else, skip object
#   if candidates length === 0 exit algorithm. (quick return)
#   go to candidates[0].rules and find first predicate with flag === 0, ask user input for that predicate
#       TO DO: try a random index, not [0]
#   repeat


def algo():
    global inpQ, inpA, candidates
    while True:
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
            print('done')
            return

        random_index = random.randint(0, interm.__len__() - 1)
        for predicate in interm[random_index]['rules'].keys():
            if not interm[random_index]['rules'][predicate]['flag']:
                inpQ = predicate
                # inpA = interm[random_index]['rules'][predicate]['value']
                inpA = input(predicate)
                break
        candidates = interm


def show_results():
    if results.__len__() == 0:
        print("GET A BIKE")

    for entry in results:
        print(entry['car']['name'])
        print(entry['car']['description'])


init()
# algo()
# show_results()

# create text labels
# tk.Label(frame, textvariable=questionLabel, fg=text_color, bg=window_background, justify='left', anchor='w', font=("Courier", 21)).grid(
#     row=0, column=0)

# add title to window
root.wm_title("Car Recommendation Expert System")
question_label_text.set("a")


def test():
    question_label_text.set("b")


# # call looping function after 1000ms
root.after(3000, test)

main = MainView(root)

main.pack(side="top", fill="both", expand=True)
root.wm_geometry("400x400")

# make sure program does not stop until closed by user
root.mainloop()
