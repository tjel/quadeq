import math
import sys

#a,b,c = input("Enter the coefficients of a, b and c separated by commas: ")
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

print "Solving {}x^2+{}x+{} = 0".format(a,b,c)

d = b**2-4*a*c # discriminant

if d < 0:
    print "This equation has no real solution"
elif d == 0:
    x = (-b) / (2 * a)

    print "This equation has one solutions: ", x
else:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)

    print "This equation has two solutions: ", x1, " and", x2

x ,y ,z = 2, 7, 3     
delta = y**2-4*x*z
X1 = (-y + math.sqrt(delta)) / (2 * x)
X2 = (-y - math.sqrt(delta)) / (2 * x)

print 'Test case: For x = {}, y = {}, z = {} solutions are: {} and {}'.format(x,y,z,X1,X2)
