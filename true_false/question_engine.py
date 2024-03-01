# # Engine to Create new Question, Add Scores, and Check if the answer is correct or not
from question_model import Question_model


class question_engine:
    score = 0
    question = None

    def __init__(self):
        self.score = 0

    def createQuestion(self):
        self.question = Question_model()
        return self.question.question_word

    def checkAnswer(self, player_answer):
        if self.question.question_answer.lower() == player_answer:
            self.addScore()
        else:
            print(f"You got it Wrong\nYour Final Score is {self.score}")
            quit()

    def addScore(self):
        self.score = self.score + 1
