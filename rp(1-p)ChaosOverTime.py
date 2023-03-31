from PIL import Image
import numpy as np
import random
#Use numpy arrays for speed 
x = np.array([])
y = np.array([])

width = 1920
height = 1080
#Scale factor to scale image res to the section of the diagram that shows chaos
xSF = 1.5 / width
ySF = 1 / height

#Generate random points for initial iteration (n=0)
for i in range(100000):
    x = np.append(x, random.randint(2500,4000)/1000)
    y = np.append(y, random.randint(1,1000)/1000)

#Change plateaus around 35 iterations
#Iterate over the random points applying the equation
for m in range(35):
    for k in range(len(x)):
        r = x[k]
        p = y[k]
        for j in range(m):
            p = r * p * (1-p)
        y[k] = p
    #Saving an image for an animation after each iteration
    #Change values of output image for places visited by the iterations to white
    im = Image.new('RGB', (width, height))
    pix = im.load()
    for i in range(len(x)):
        xVal = int(round(((x[i] - 2.5)/xSF),0))-1
        yVal = int(round((y[i] / ySF),0))-1
        pix[xVal, yVal] = (255,255,255)
    im.save(f'Chaos_{m}.png', 'PNG')
