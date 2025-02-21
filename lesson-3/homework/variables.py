###Given two integer variables: a and b. Swap the values of the variables.
a = int(input())
b = int(input())

# write code here. Don't change given conditions

print(a, b)

Solve this problem in 3 ways
1.
a = int(input())
b = int(input())

a,b = b, a

a,b

2.

a = int(input())
b = int(input())

c= a
a = b
b = c

a,b

3.

a = a+b
b = a-b
a = a-b

a,b
