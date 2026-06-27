from tkinter import *

THEME_COLOR = "#1F3A4D"
CANVAS_COLOR = "#EAF4F4"
FONT = ("Arial", 28, "normal")


class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Country Capital Quiz")
        self.window.minsize(width=1000, height=1000)
        self.window.config(padx=50, pady=40, bg=THEME_COLOR)

        self.window.grid_columnconfigure(0, weight=1, uniform="buttons")
        self.window.grid_columnconfigure(1, weight=1, uniform="buttons")

        self.score_label = Label(
            text="Score: 0",
            font=FONT,
            fg="white",
            bg=THEME_COLOR,
        )
        self.score_label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="e",
            pady=(0, 30),
        )

        self.canvas = Canvas(
            width=800,
            height=500,
            bg=CANVAS_COLOR,
            highlightthickness=0,
        )
        self.question_text = self.canvas.create_text(
            400,
            250,
            width=720,
            text="Question",
            fill=THEME_COLOR,
            font=FONT,
            justify="center",
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(0, 45))

        self.true_image = PhotoImage(file="images/true.png").subsample(5, 5)
        self.true_button = Button(
            image=self.true_image,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            relief=FLAT,
            borderwidth=0,
            highlightthickness=0,
            padx=0,
            pady=0,
        )
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="images/false.png").subsample(5, 5)
        self.false_button = Button(
            image=self.false_image,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            relief=FLAT,
            borderwidth=0,
            highlightthickness=0,
            padx=0,
            pady=0,
        )
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
