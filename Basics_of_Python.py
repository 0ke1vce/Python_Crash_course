print("Hello world")
# comments are the line are of which are not executed by interpreter.
# comments -->
# 1- Single line comment by #
# 2- Multi Line comment by """"""
"""This is a multi line comment"""

# Variables in Python->
a = 3
print(a)  # it will print 3
b = 55
print(b)  # it will print 55
a = 6.2  # it is a floating point number --> integer with decimal point
print(a)
c = "Harry"  # it is a string which is a sequence of character
print(c)
d = True  # or False   True/False are boolean data type
print(d)

# Type Casting in Python
"""
Type casting simply means changing one data type to another.
String and int cannot be concatenate.  (it means add)
string and string cannot be replicate.  (it means Multiply)
"""
f = "5"
print(int(f)+1)  # it will convert string f("5") to integer 5 and add 1


# Operator in Python
num1 = 10
num2 = 2
"""
Arithmatic operator --> +,-,*,/,%
"""
print("num1 + num2 ", num1+num2)
print("num1 - num2 ", num1-num2)
print("num1 * num2 ", num1*num2)
print("num1 / num2 ", num1/num2)
print("num1 % num2 ", num1 % num2)
print("num1 to the power num2 ", num1 ** num2)
print("num1 // num2 ", num1 // num2)

"""
Assignment operator--> =,+=,-=,*=,/=,%=
"""
a = 5
a += 1
a -= 1
a *= 1
a /= 1
a %= 1

"""
Comparison operator--> Give true or false --> >,<,==,!=,>=,<=
"""
x = 5
y = 3
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

"""
Logical Operator--> and,or,not
"""
x = 3
y = 4
print(x > y and y < x)
print(x > y or y > x)
print(not False)




