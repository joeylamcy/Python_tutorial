# Objective: Solve the quadratic equation ax**2 + bx + c = 0

# import library
import numpy as np

# set the values of coefficients
a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-np.sqrt(d))/(2*a)
sol2 = (-b+np.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
