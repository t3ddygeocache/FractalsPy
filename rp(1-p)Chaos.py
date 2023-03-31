from PIL import Image
import numpy as np

#Use numpy arrays for speed 
x = np.array([])
y = np.array([])

#Detail is the completeness of the output
#100 is max but takes long time, 5 seems best
#Samples is how granular the scale is, 1000 is good
width, height = 1920, 1080
height = 1080
detail = 5
detail = 1 - detail / 100
samples = 1000
#Scale factor to scale image res to the section of the diagram that shows chaos
xSF = 1.5 / width
ySF = 1 / height

#Iterate the equation and take the last few results to plot to show the oscillations
def iterate(r, x, y, iterations):
    p = 0.02
    for i in range(iterations):
        p = r * p * (1-p)
        if i > detail*samples:
            x = np.append(x, r)
            y = np.append(y, p)
    return x,y
#Find the values for small increments of r (x axis) depending on sample number
for i in range(int(2.5*samples), int(4*samples), 1):
    vals = iterate(i/samples, x,y, 1000)
    x,y = vals[0], vals[1]
    
im = Image.new('RGB', (width, height))
pix = im.load()
#Change values of output image for places visited by the iterations to white
for i in range(len(x)):
    xVal = int(round(((x[i] - 2.5)/xSF),0))
    yVal = int(round((y[i] / ySF),0))
    pix[xVal, yVal] = (255,255,255)
                     
im.save('Chaos.png', 'PNG')
