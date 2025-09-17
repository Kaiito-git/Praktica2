from math import *
x=1.825*10**2
y=18.225
z=-3.298*10**-2
p = y/x
l = y-x
s = (abs(x**p - p**(1/3)) + l * ((cos(y) - (z/l))/(1+(l)**2)))
print(s)
