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
    self.start_time = datetime.datetime.now()

    for question in self.questions:
      self.answers.append(self.ask(question))
    
  def ask(self, question):
    correct = False
    question_start = datetime.datetime.now()
    answer = input(question.text + ' = ')
    
    if answer == str(question.answer):
      correct = True
    
    question_ end = datetime.datetime.now()
    return correct, question_end - question_start

  def summary(self):
    print(f'You got {self.total_correct()} out of {self.questions} right.')
    print(f'It took you {self.end_time - self.start_time} seconds total.')
