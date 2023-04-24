import math, pygame, time

width, height = 1600, 800
maxLen = (width**2+height**2)**0.5
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Raycasting')
clock = pygame.time.Clock()
running = True
screen.fill((0,0,0))

class Player:
    def __init__(self,startX, startY):
        self.x = startX
        self.y = startY
    def moveX(self, delta):
        self.x += delta
        return self.x
    def moveY(self, delta):
        self.y += delta
        return self.y
    def retrieveCoords(self):
        return (self.x, self.y)
    def draw(self):
        pygame.draw.ellipse(screen, (255,255,255), (self.x, self.y,  20,20))
    def calcMove(self, direction):
        distance = 10
        self.theta = math.radians(cam.retrieveAngle() + (cam.retrieveFov() / 2) - 180)
        if direction == 'w':
            xVal = 0
            yVal = 10
            moveAmtX = xVal * math.cos(self.theta) - yVal * math.sin(self.theta)
            moveAmtY = (yVal * math.cos(self.theta) + xVal * math.sin(self.theta))*-1
        elif direction == 'a':
            xVal = -10
            yVal = 0
            moveAmtX = xVal * math.cos(self.theta) - yVal * math.sin(self.theta)
            moveAmtY = (yVal * math.cos(self.theta) + xVal * math.sin(self.theta))*-1
        elif direction == 's':
            xVal = 0
            yVal = -10
            moveAmtX = xVal * math.cos(self.theta) - yVal * math.sin(self.theta)
            moveAmtY = (yVal * math.cos(self.theta) + xVal * math.sin(self.theta))*-1
        elif direction == 'd':
            xVal = 10
            yVal = 0
            moveAmtX = xVal * math.cos(self.theta) - yVal * math.sin(self.theta)
            moveAmtY = (yVal * math.cos(self.theta) + xVal * math.sin(self.theta))*-1
        
        moveAmtX = int(round(moveAmtX,0))
        moveAmtY = int(round(moveAmtY,0))
        self.moveX(moveAmtX)
        self.moveY(moveAmtY)

def findIntersection(x1,y1,x2,y2,x3,y3,x4,y4, angle):
    try:
        xCoords = [x1, x2, x3, x4]
        xCoords = [math.floor(x) for x in xCoords]
        px=( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
        py= ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
        if round(x1,0) == round(px,0) and round(x2,0) == round(px,0) and ((x3>px and x4<px)or(x3<px and x4>px)) and ((y1>py and y2<py)or(y1<py and y2>py)):
            return (True, px, py)
        if x1 > px and x2 < px:
            if x3 > px and x4 < px:
                return (True, px, py)
            elif x3 < px and x4 > px:
                return (True, px, py)
            else:
                return(False,px)
        elif x1 < px and x2 > px:
            if x3 > px and x4 < px:
                return (True, px, py)
            elif x3 < px and x4 > px:
                return (True, px, py)
            else:
                return(False,px)
        else:
            return(False,px)
    except ZeroDivisionError:
        return (False,x1)

class Ray:
    def __init__(self, x,y,angle):
        self.xVal = x
        self.yVal = y
        self.angle = math.radians(angle)
        self.refAngle = angle
        self.endX = x
        self.endY = y
        self.maxLen = maxLen = (width**2+height**2)**0.5
        self.col = (255, 255, 255)
        self.hitCol = [255, 255, 255]
    def setCoords(self, x,y):
        self.xVal = x
        self.yVal = y
    def calcLine(self, x,y,angle,maxLen):
        self.endX = math.sin(self.angle)*self.maxLen + self.xVal
        self.endY = math.cos(self.angle)*self.maxLen + self.yVal
        for i in boundaries:
            bVals = boundaries[i].retrieveCoords()
            vals = findIntersection(self.xVal, self.yVal, self.endX, self.endY, bVals[0],bVals[1],bVals[2],bVals[3], self.angle)
            if vals[0]:
                self.endX = vals[1]
                self.endY = vals[2]
                self.hitCol = boundaries[i].retrieveCol()
    def draw(self):
        self.calcLine(self.xVal, self.yVal, self.angle, self.maxLen)
        #pygame.draw.line(screen, self.col, (self.xVal,self.yVal), (self.endX, self.endY), width=1)
    def retrieveCoords(self):
        return(self.xVal, self.yVal, self.endX, self.endY)
    def retrieveHitCol(self):
        return self.hitCol

class Boundary:
    def __init__(self, x, y, endX, endY, col):
        self.x = x
        self.y = y
        self.endX = endX
        self.endY = endY
        self.col = col
    def retrieveCoords(self):
        return(self.x,self.y,self.endX,self.endY)
    def retrieveCol(self):
        return self.col
    def draw(self):
        pygame.draw.line(screen, (self.col[0],self.col[1],self.col[2]), (self.x,self.y), (self.endX, self.endY), width=3)

class Camera:
    def __init__(self, angleFacing, fov):
        self.angleFacing = angleFacing
        self.fov = fov
    def retrieveAngle(self):
        return self.angleFacing
    def retrieveFov(self):
        return self.fov
    def updateAngle(self, delta):
        self.angleFacing += delta
    def setAngle(self, angle):
        self.angleFacing = angle
        
player = Player(width/4,height/2)
raySize = 0.5
boundaries = {
    'boundary1': Boundary(300,600, 200, 450, [255,0,0]),
    'boundary2': Boundary(100, 100, 501, 101, [0,255,0]),
    'boundary3': Boundary(550, 90, 551, 300, [0,0,255])
    }
rays = {}
for i in range(int(360/raySize)):
    rays[f'ray{i}'] = Ray(width/2,height/2,i*raySize)
press = time.time()
cam = Camera(140, 80)
fov = cam.retrieveFov()
rectWidth = (width/2)/fov
distCoeff = -0.005
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_c]:
                pygame.quit()
                exit()
            elif pressed[pygame.K_q]:
                if time.time() - press > 0.1:
                    cam.updateAngle(4)
                    press = time.time()
            elif pressed[pygame.K_e]:
                if time.time() - press > 0.1:
                    cam.updateAngle(-4)
                    press = time.time()
            elif pressed[pygame.K_w]:
                player.calcMove('w')
            elif pressed[pygame.K_a]:
                player.calcMove('a')
            elif pressed[pygame.K_s]:
                player.calcMove('s')
            elif pressed[pygame.K_d]:
                player.calcMove('d')
            elif pressed[pygame.K_r]:
                cam.setAngle(140)
            playerPos = player.retrieveCoords()    
            screen.fill((0,0,0))
            for i in rays:
                rays[i].setCoords(playerPos[0],playerPos[1])
                rays[i].draw()
            for i in boundaries:
                boundaries[i].draw()        
        pygame.draw.rect(screen,(0,0,0),(width/2,0,width/2,height))
        angleFacing = cam.retrieveAngle()
        for i in range(int(fov/raySize)):
            rayKey = i + int(angleFacing/raySize)
            vals = rays[f'ray{rayKey}'].retrieveCoords()
            x, y, endX, endY = vals[0], vals[1], vals[2], vals[3]
            eucDist = round((x-endX)**2 + (y-endY)**2, 0)
            manDist = round(abs(x-endX) + abs(y-endY),0)
            dist = manDist 
            hitCol = rays[f'ray{rayKey}'].retrieveHitCol()
            rectColCoeff = 2**(dist*distCoeff)
            rectCol = (int(round(rectColCoeff*hitCol[0],0)), int(round(rectColCoeff*hitCol[1],0)), int(round(rectColCoeff*hitCol[2],0)))
            rectHeight = int(round(height * rectColCoeff,0))
            if vals[2] < 0 or vals[2] > width or vals[3] < 0 or vals[3] > height:
                dist = 0
            pygame.draw.rect(screen, rectCol, (width-i*rectWidth*raySize-rectWidth, int(round(0.5*(height-rectHeight),0)), rectWidth*raySize, rectHeight))
    player.draw()        
    pygame.display.update()
pygame.quit()
