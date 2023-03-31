from PIL import Image
from numba import njit

#Named values of c that give fractals
cVals = {
    'Douady Rabbit' : complex(-0.123, 0.745),
    'San Marco' : complex(-0.75, 0),
    'Siegel Disk' : complex(-0.391, -0.587)
    }

width, height = 3840, 2400

#Used to find position of points in relation to center of image
xMid = width // 2
yMid = height // 2
#Scales the image so the axis are lower to make the set visible
xDivFactor = width / 3
yDivFactor = height / 2

im = Image.new("RGB", (width, height))
pix = im.load()

#Given the coordinates of a point, iterate z**2 + c to see if it goes to infinity
#Fractal is on complex plane so treat y axis as imaginary numbers
#Use JIT compiler to accelerate calculations by about 700%
@njit
def calcJulia(x,y, maxIts, c):
    z = complex(x/xDivFactor, y/yDivFactor)
    for k in range(maxIts):
        z = z**2 + c
        if abs(z) > 2:
            #Nice cyan colour, intensity depends on how quickly z**2 + c increases past 2
            return ((0, k*10, k*20))
    #If it stays less than 0, it is inside the bulb so remain black
    return ((0,0,0))

def julia(c):
    #For each pixel in the image, find if it is part of the set and colour the pixel accordingly
    maxIts = 50
    for i in range(width):
        x = i - xMid
        for j in range(height):
            pix[i,j] = calcJulia(x,j - yMid, maxIts, c)
    #Write the pixels to a PNG in the same directory as the python file, called Julia
    im.save(f"Julia_{c}.png", "PNG")

if __name__ == '__main__':
    julia(cVals['San Marco'])
    
