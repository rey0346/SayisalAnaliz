import math
a=math.pi/5
x=math.cos(a)
y=math.cos(0)-(math.sin(0)*(a-0))
birlihata=x-y
print('bir terimli taylor seri acilimindaki kesme hatasi:',birlihata)
z=math.cos(0)-(math.sin(0)*(a-0))-(math.cos(0)*a*a/2)
ikilihata=x-z
print('iki terimli taylor seri acilimindaki kesme hatasi:',ikilihata)