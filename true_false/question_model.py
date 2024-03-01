# # To Make A Question with 2 Variabels, A Question and An Answer
from data import question_data as question_data
import random as rand


class Question_model:
    question_word = ''
    question_answer = ''

    def __init__(self):
        question = rand.choice(question_data)
        self.question_word = question['question']
        self.question_answer = question['correct_answer']

    def printQuestion(self):
        print(self.question_word)
