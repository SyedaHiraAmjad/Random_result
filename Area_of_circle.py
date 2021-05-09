'''Python: Area of a Circle
In geometry, the area enclosed by a circle of radius r is πr2. 
Here the Greek letter π represents a constant, approximately equal to 3.14159, 
which is equal to the ratio of the circumference of any circle to its diameter.'''
#Solution:
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
