# built-in
import datetime
import random
# my-own
from questions import Add, Multiply


class Quiz:
  questions = []
  answers = []
  
  def __init__(self):
    question_types = (Add, Multiply)
    for _ in range(10):
      num1 = random.randint(1, 10)
      num2 = random.randint(1, 10)
      question = random.choice(question_types)(num1, num2)
      self.questions.append()
    
  def take_quiz(self):
    pass
    
  def ask(self, question):
    pass
  
  def total_correct(self):
    total = 0
    for answer in self.answers:
      if answer[0]:
        total += 1
    return total

  def summary(self):
    print(f'You got {self.total_correct()} out of {self.questions} right')
    print(f'It took you {(self.end_time-self.start_time).seconds} seconds total.')
