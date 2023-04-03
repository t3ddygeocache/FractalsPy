#Pi estimate using https://en.wikipedia.org/wiki/Buffon%27s_needle_problem
import math, pygame, random

width, height = 1000, 1000
#t is the spacing of the vertical lines
t = 10
#l is the length of each needle
l = 9

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Buffon\'s Needles')
clock = pygame.time.Clock()
running = True
screen.fill((0, 0, 0))

#Draw initial vertical lines
for i in range(t, width, t):
    pygame.draw.line(screen, (255,255,255), (i, 0), (i, height))
    
crossing = 1
notCrossing = 1
while running:
    for j in range(500):
        #Randomly place and angle the needles within the window
        randX = random.randint(0, width)
        randY= random.randint(0, height)
        randTheta = math.radians(random.randint(-90, 90))
        #Find horizontal and vertical lengths accounting for rotation of needle
        yLen = math.sin(randTheta) * l * 0.5
        xLen = math.cos(randTheta) * l * 0.5
        #Check if the horizontal length crosses a vertical line
        #Update total for crossing or not crossing and draw the needle
        for i in range(int(width / t)):
            if randX - xLen < i*t and randX + xLen > i*t:
                pygame.draw.line(screen, (0,255,0), (randX-xLen, randY-yLen), (randX + xLen, randY+yLen))
                crossing += 1
                break
        else:
            pygame.draw.line(screen, (255,255,255), (randX-xLen, randY-yLen), (randX + xLen, randY+yLen))
            notCrossing += 1
    #Use ratio of needles crossing lines to total to approximate the probability
    #Use (2l)/(pi*t) = P to estimate pi
    pygame.draw.rect(screen, (0,0,0), (0, height*0.9, width, height*0.1))
    piEst = (2*l) / ((crossing/(notCrossing+crossing))*t)
    #Draw estimate of pi to bottom of the screen, centred
    font = pygame.font.SysFont(None, 72)
    img = font.render(str(round(piEst, 5)), True, (255,255,255))
    img_rect = img.get_rect(center=(width/2, height - 50))
    screen.blit(img, img_rect)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
