from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, 'italic')


class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text=f'Some question text',
                                                     font=FONT,
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="", pady=20, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        false = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false, command=self.false_answer)
        self.false_button.grid(column=1, row=3)

        true = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true, command=self.true_answer)
        self.true_button.grid(column=0, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end!")
            self.true_button.config(state='disabled')
            self.true_button.config(state='disabled')

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
        self.window.after(1000, self.get_next_question)
