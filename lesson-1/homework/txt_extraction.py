#   given a side of squere. find its perimetr

a = int(input("Kvadratni tomonini kiriting:"))
b = 4 * a
c = pow(a, 2)
print("perimetri ", b, "ga teng, Yuzi ", c, "ga teng")

#   given diameter of circle. Find its length.
import math

a = int(input("Diameterni kiriting: "))
r = a/2
p = math.pi
l = 2 *p *r

print("Aylananing uzunligi ", l, " ga teng")

#   given two numbers a and b. Find their mean.

a = int(input("birinchi sonni kiriting: "))
b = int(input("birinchi sonni kiriting: "))
result = (a + b) / 2
result

#given two numbers a and b. Find their sum, product and square of each number.

a = int(input("birinchi sonni kiriting: "))
b = int(input("birinchi sonni kiriting: "))
summ = a + b
product = a * b
square1 = pow(a, 2)
square2 = pow(b, 2)

print(summ, product, square1, square2)
