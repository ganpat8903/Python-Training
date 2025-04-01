# Mathematical operators
print("Mathematical operators".center(100,"-"))
a = 7
b = 4

c = a + b
print("c = a + b: \n{}\n".format(c))

c = a - b
print("c = a - b: \n{}\n".format(c))

c = a * b
print("c = a * b: \n{}\n".format(c))

c = a ** b
print("c = a ** b: \n{}\n".format(c))

c = a / b
print("c = a / b: \n{}\n".format(c))

c = a // b
print("c = a // b: \n{}\n".format(c))

c = a % b
print("c = a % b: \n{}\n".format(c))

c = a + (-b)
print("c = a + (-b): \n{}\n".format(c))

c = (-a) + b
print("c = (-a) + b: \n{}\n".format(c))

# Bitwise operators
print("Bitwise operators".center(100,"-"))
a = 7
b = 4
c = a << 2
print("c = a << 2: \n{}\n".format(c))

c = b >> 2
print("c = b >> 2: \n{}\n".format(c))

c = a & b
print("c = a & b: \n{}\n".format(c))

c = a | b
print("c = a | b: \n{}\n".format(c))

c = a ^ b
print("c = a ^ b: \n{}\n".format(c))

# Comparison operators
print("Comparison operators".center(100,"-"))
a = 7
b = 7.0
print("a == b: \n{}\n".format(a == b))
print("a is b: \n{}\n".format(a is b))

a = [1, 2, 3, 4]
b = 3
c = 5
print("b in a: \n{}\n".format(b in a))
print("c in a: \n{}\n".format(c in a))

a = "python"
b = "th"
c = "xyz"
print("b in a: \n{}\n".format(b in a))
print("c in a: \n{}\n".format(c in a))

# Logical operators
print("Logical operators".center(100,"-"))
print("and".center(50,"*"))
print("Input \t\t Input \t\t output\n")
print("True \t\t True \t\t {}\n".format(True and True))
print("True \t\t False \t\t {}\n".format(True and False))
print("False \t\t True \t\t {}\n".format(False and True))
print("False \t\t False \t\t {}\n".format(False and False))

print("or".center(50,"*"))
print("Input \t\t Input \t\t output\n")
print("True \t\t True \t\t {}\n".format(True or True))
print("True \t\t False \t\t {}\n".format(True or False))
print("False \t\t True \t\t {}\n".format(False or True))
print("False \t\t False \t\t {}\n".format(False or False))

print("not".center(50,"*"))
print("Input \t\t output\n")
print("True \t\t {}\n".format(not True))
print("False \t\t {}\n".format(not False))

# Operator precendence
print("Operator precendence".center(100,"-"))
a = 10
b = 7
c = 13
print("a * b + c: {}\n".format(a * b + c))
print("a + b * c: {}\n".format(a + b * c))
print("a * (b + c): {}\n".format(a * (b + c)))

# Associativity
print("Associativity".center(100,"-"))
# since the ** operator has right-to-left associativity
a = 10
b = 3
c = 2
print(a ** b ** c) # will be executed as (a ** (b ** c))

# since the / operator has left-to-right associativity
a = 12
b = 3
c = 4
print(a / b / c) # will be executed as ((a / b) / c)

print(2018 % 4 == 0 and 2018 % 100 != 0 or 2018 % 400 == 0)

# Exercise
x = 17 / 2 * 3 + 2
print(x)

x = 2 + 17 / 2 * 3
print(x)

x = 19 % 4 + 15 / 2  * 3
print(x)

x = (15 + 6) - 10 * 4
print(x)

x = 17 / 2 % 2 * 3**3
print(x)

a,b,c,d,e=1,2,3,4,5
x = a ** b % c / d + e * b ** a
print(x)

x = a * b ** 2 + c ** 3
print(x)
