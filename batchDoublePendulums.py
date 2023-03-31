#Maths from https://www.myphysicslab.com/pendulum/double-pendulum-en.html
import math, pygame, random

width, height = 900, 900
g = 1
x0 = width / 2
y0 = height / 2 

class Pendulum:
    def __init__(self, r1, r2, ang1, ang2, m1, m2, col, ang1Vel, ang2Vel):
        #Define the pendulum's lengths, masses, initial angles and velocities
        self.r1 = r1
        self.r2 = r2
        self.ang1 = ang1
        self.ang2 = ang2
        self.m1 = m1
        self.m2 = m2
        self.col = col
        self.ang1Vel = ang1Vel
        self.ang2Vel = ang2Vel

    def update(self):
        #Find the x and y locations of the ends of the pendulum according to the angle from the y axis
        self.x1 = math.sin(self.ang1) * self.r1
        self.y1 = math.cos(self.ang1) * self.r1
        self.x2 = math.sin(self.ang2) * self.r2
        self.y2 = math.cos(self.ang2) * self.r2

        #Find the angular acceleration of the upper pendulum
        num1 = -g * (2 * self.m1 + self.m2) * math.sin(self.ang1)
        num2 = -(self.m2) * g * math.sin(self.ang1 - 2 * self.ang2)
        num3 = -2 * math.sin(self.ang1 - self.ang2) * self.m2 * (self.ang2Vel ** 2 * self.r2 + self.ang1Vel **2 * self.r1 * math.cos(self.ang1 - self.ang2))
        num4 = self.r1 * (2 * self.m1 + self.m2 - self.m2 * math.cos(2 * self.ang1 - 2 * self.ang2))
        self.ang1Acc = (num1 + num2 + num3) / num4
        #Find the angular acceleration of the lower pendulum
        num1 = 2 * math.sin(self.ang1 - self.ang2)
        num2 = self.ang1Vel **2 * self.r1 * (self.m1 + self.m2) + g * (self.m1 + self.m2) * math.cos(self.ang1) + self.ang2Vel **2 * self.r2 * self.m2 * math.cos(self.ang1 - self.ang2)
        num3 = self.r2 * (2 * self.m1 + self.m2 - self.m2 * math.cos(2 * self.ang1 - 2 * self.ang2))
        self.ang2Acc = (num1 * num2) / num3
        #Alter the angle and velocity of the pendulums according to previously calculated accelerations
        self.ang2Vel += self.ang2Acc
        self.ang1Vel += self.ang1Acc
        self.ang1 += self.ang1Vel
        self.ang2 += self.ang2Vel
        
    def draw(self):
        self.update()
        #Draw the ellipses as the masses connected by lines
        pygame.draw.ellipse(screen, self.col, (self.x1+x0-(self.m1/4), self.y1+y0-(self.m1/4), self.m1/2, self.m1/2))
        pygame.draw.ellipse(screen, self.col, (self.x2+self.x1+x0 - (self.m2/4), self.y2+self.y1+y0-(self.m2/4), self.m2/2, self.m2/2))
        pygame.draw.line(screen, self.col, (x0, y0), (self.x1+x0,self.y1+y0), width = 3)
        pygame.draw.line(screen, self.col, (self.x1+x0, self.y1+y0), (x0+self.x1+self.x2,y0+self.y1+self.y2), width = 3)
        
#Iteratively create a batch of pendulums with subtlely different starting angles to show sensitivity to inital conditions, random colour to differentiate between pendulums easier
pendulums = {}
for i in range(1000):
    pendulums[f'Pen{i}'] = Pendulum(200, 200, math.pi - 2 - (random.randint(1,100) / 10000),math.pi - 4 - (random.randint(1,100) / 10000), 40, 40, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 0.1, 0.1)
    
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Pendulums')
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))
    #Draw the stationary point as that is shared between pendulums so should only be drawn once
    pygame.draw.ellipse(screen, (255, 255, 255), (x0-5, y0-5, 10, 10))
    #Update and draw every pendulum
    for i in pendulums:
        pendulums[i].draw()
        
    pygame.display.update()
    #45 fps seemed the best looking rate without looking too fast
    clock.tick(45)
