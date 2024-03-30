# RandomProjects
This is a repo for me to keep my random projects in one place, mostly maths stuff like fractals and simulations

Explanations:

BuffonsNeedlePiApprox

Finding an approximation for pi using Buffon's Needle problem:

https://en.wikipedia.org/wiki/Buffon%27s_needle_problem

Simulate many needle drops, use the ratio of needles crossing a line between strips to the total number of needles to approximate the probability. As the probability = (2 * length of needle) / (width of wood strip * pi), the formula can be rearranged to pi = (2 * length of needle) / (probability * width of wood strip), converges to pi for many needles. No files produced, visualisation using PyGame

JuliaSet

https://en.wikipedia.org/wiki/Julia_set

Iterate for every point on a complex plane (using x axis as real numbers and y axis as imaginary component), z = z ** 2 + c where c is a constant. If z goes to infinity, the point is coloured based on how quickly it increases, if it stays bound it is coloured black. Produces PNG of the fractal

Mandelbrot

https://en.wikipedia.org/wiki/Mandelbrot_set

For every point on the complex plane (x as real, y as imaginary, iterate z ** 2 + c where z starts as 0 and c is the complex coordinate of the point. If it goes to infinity, colour base on rate of increase, if it stays bound then coloured black. Produces PNG of the fractal

batchDoublePendulums

https://www.myphysicslab.com/pendulum/double-pendulum-en.html

Simulates many double pendulums with very similar intitial conditions, showing how they move and diverge over time creating chaos. No files produced, uses PyGame to visualise all the pendulums

rp(1-p)Chaos

https://en.wikipedia.org/wiki/Logistic_map

Creates bifurcation diagram of logistic map of rp(1-p) which shows periodic doubling producing chaos. Uses x axis for r and y axis for p, iterates p = rp(1-p) and plots the points it oscillates between, as it goes from initially stable for low r to oscillating between 2 values until eventually chaos for higher values of r. Produces PNG of the final bifurcation diagram

rp(1-p)ChaosOverTime 

Same as rp(1-p)Chaos in principle. Creates thousands of random points for r and p, iterates each point and produces an image for each iteration to show the values converging on the final bifurcation diagram. Produces many PNGs of the bifurcation diagram, one for each iteration

