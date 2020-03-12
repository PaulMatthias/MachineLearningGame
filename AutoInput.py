from random import seed
from random import random

class AutoInput:
    def __init__(self):
        seed(1)
        self.key = ''

    def generateRandomKeyPress(self):
        rndNumber = random()
        if rndNumber < 0.2:
            self.key = 'LEFT'
        elif rndNumber < 0.8:
            self.key = 'RIGHT'
        else:
            self.key = 'UP'

