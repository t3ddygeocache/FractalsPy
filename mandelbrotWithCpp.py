import os
from PIL import Image

prog = 'mandelbrot.cpp'
os.system(f'g++ {prog} -O3 -o mandelbrot.out')
os.system('./mandelbrot.out')

with open('mandelbrotVals.txt', 'r') as f:
    vals = f.read()
    
allVals = vals.split(',')[:-1]
width = int(allVals[0])
height = int(allVals[1])
allVals = allVals[2:]

im = Image.new('RGB', (width, height))
pix = im.load()

for i in range(len(allVals)):
    k = int(allVals[i])
    x = i % width
    y = i // width
    pix[x,y] = ((0, k*20, k*40))
    
im.save('Mandelbrot.png', 'PNG')