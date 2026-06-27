from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "normal")


class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Country Capital Quiz")
        self.window.minsize(width=500, height=500)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text="Score: 0",
            font=FONT,
            fg="white",
            bg=THEME_COLOR,
        )
        self.score_label.grid(row=0, column=0, columnspan=2, sticky="e", pady=(0, 20))

        self.canvas = Canvas(
            width=400,
            height=250,
            bg="white",
            highlightthickness=0,
        )
        self.question_text = self.canvas.create_text(
            200,
            125,
            width=360,
            text="Question",
            fill=THEME_COLOR,
            font=FONT,
            justify="center",
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(0, 25))

        self.true_image = PhotoImage(file="images/true.png").subsample(10, 10)
        self.true_button = Button(
            image=self.true_image,
            borderwidth=0,
            highlightthickness=0,
        )
        self.true_button.grid(row=2, column=0, padx=20)

        self.false_image = PhotoImage(file="images/false.png").subsample(10, 10)
        self.false_button = Button(
            image=self.false_image,
            borderwidth=0,
            highlightthickness=0,
        )
        self.false_button.grid(row=2, column=1, padx=20)

        self.window.mainloop()
