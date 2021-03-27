# cres
Car Recommendation Expert System

## Intro

C.R.E.S. is an expert system application that, based on the user's answers to a series of questions, recommends one or more cars that suit his/her requirements.

## Use

![cres](https://user-images.githubusercontent.com/33568824/112727090-6ec88c00-8f29-11eb-8980-5225853c21c9.jpg)


First off, in order to be able to run the application, you need to have Python 3 and the package `Pillow` installed on the computer.

To start the application, run `python3 main.py` in your favorite CLI.

Once the application is opened, the welcome page will appear on the screen, waiting for the user to press the `“Begin”` button.

After the user starts the process, he/she is asked a series of grid-type questions with an answer in order to gather as much information as possible to make the best car recommendation the system can.

When the process finishes (either it finds the user one or more cars that would suit him/her, or no car in the knowledge base meets his/her needs), it will display the results screen that will contain either a list with a photo of the car, its name and a short description, or a message in which it "explains" to the user that it could not find a suitable result and a photo with a means of public transport. When hovering the cursor over an image, the application will show how it came to that conclusion.

## Implementation

C.R.E.S. was implemented in Python, using `tkinter` for the graphical interface and `Pillow` for working with image files. It uses the forward-chaining technique to make car suggestions: it receives a series of premises as input and, based on predefined rules, tries to draw a conclusion.


The knowledge base, which sits at the base of the expert system, contains a series of 68 such inputs, one for each car. These objects contain a `“rules”` property in which the activation rules for the respective cars are defined and a `“car”` property in which the details of the car are defined.

```
{
	 "rules":{
		"why":"transport",
		"care_about":"what_people_think_of_me",
		"want_think":"i_seem_rich",
		"hope_you_like_debt":"love_it"
	 },
	 "car":{
		"id":"mercedes_cls",
		"name":"MERCEDES CLS",
		"description":"The Mercedes CLS is a stylish, quick and comfortable executive saloon with room for four passengers and their luggage. The Mercedes CLS is a sleek, low-slung four-door luxury coupe that's designed to blend desirability with practicality."
	 }
},
```


When opening the application, all the rules from the knowledge base are loaded in its memory in a one-dimensional table named `candidates`, as well as the data from the file containing the `“String”` type sequences that are displayed in the forms.

After the user presses the `“Begin”` button, the first question addressed to him is the one corresponding to the predicate `“why”` which is found on every car in the knowledge base. After the user responds, the application goes through the `candidates` array and, if the user's answer matches the rule from that car, it will set a `flag` next to it as `1` (true), otherwise the car will be removed from the `candidates` table. If all the rules of a car have `flag: 1`, the car will move to the `results` array. When it finishes, it will choose a car at random and try to activate another one of its rules.

This is repeated until the `candidate` array is emptied. At this point, the application switches to the results screen where it will display each car in the `results` array or, if it is empty, will display another message.


The way the app works is also explained graphically with the help of the flowchart below.

![pill reminder flowchart (1)](https://user-images.githubusercontent.com/33568824/112726523-8eaa8080-8f26-11eb-9c36-c8225bd2e3ae.png)

Basically, the application tries to activate the rules of each car progressively. If the user's response does not match the rule that the application is trying to activate, it completely abandon that car as a potential candidate. Also, by randomly choosing the next rule it is trying to activate, the “form” that the user fills out will not always be identical from one app run to another.
