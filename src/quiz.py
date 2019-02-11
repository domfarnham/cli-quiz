# built-in
import datetime
import random
# my-own
from questions import Add, Multiply


class Quiz:
  questions = []
  answers = []
  
  def __init__(self):
    pass
    
  def take_quiz(self):
    pass
    
  def ask(self, question):
    correct = False
    question_start = datetime.datetime.now()
    answer = input(question.text + ' = ')
    
    if answer == str(question.answer):
      correct = True
    
    question_ end = datetime.datetime.now()
    return correct, question_end - question_start

  def summary(self):
    pass
