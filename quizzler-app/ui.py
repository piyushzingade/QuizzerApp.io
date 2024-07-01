THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20 , padx=20 , background=THEME_COLOR)
        self.label_score = Label(text="Score", foreground="white" , font=14 , background=THEME_COLOR)
        self.label_score.grid(row = 0 , column = 1)

        self.canvas = Canvas(width=300 , height=250 , bg="white")
        self.question_text = self.canvas.create_text(150 , 125
                                                     ,text="some" , fill=THEME_COLOR, font = ("Arial" , 20 , "italic"))
        self.canvas.grid(row = 1 , column = 0 , columnspan = 2 ,pady = 50)
        true_button = PhotoImage(file="images/true.png")

        self.true_button = Button(image=true_button , highlightthickness=0)
        self.true_button.grid(row = 2 , column = 0)


        wrong_button = PhotoImage(file="images/false.png")

        self.wrong_button = Button(image=wrong_button, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)
        # self.right_button = Button(image="images/true.png")




        self.window.mainloop()

