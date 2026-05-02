from particle import Particle

class ParticleSystem:

    def __init__(self):

        self.particles = []

    def emit(self,x,y):

        for _ in range(5):
            self.particles.append(Particle(x,y))

    def update(self,frame):

        for p in self.particles:

            p.update()
            p.draw(frame)

        self.particles = [p for p in self.particles if p.life > 0]