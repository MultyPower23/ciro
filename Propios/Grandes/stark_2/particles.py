import random

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3,3)
        self.vy = random.uniform(-3,3)
        self.life = random.randint(20,50)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1