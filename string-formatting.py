# format() method
print("format() method".center(100,"-"))
print("Let's replaces these {} with some value".format("curly braces"))
print("What if I have {} and {} braces".format(1, 2))
print("What if I have {1} and {0} braces".format(1, 2))

# conversion flags
print("conversion flags".center(100,"-"))
a = [1, 2, "µ"]
print("Convert it to string before you replace {a!s}".format(a=a))        # Calls str() on the argument first
print("Bring out the holy {b!r}".format(b=a))                       # Calls repr() on the argument first
print("More {!a}".format(a))                                            # Calls ascii() on the argument first
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.348972))

# Formatting Types
print("Formatting Types".center(100,"-"))
a = "This is left {:<20} string"
print(a.format("aligend"))

txt = "This is right {:*>20} string"
print(txt.format("aligned"))

txt = "This is center {:^20} string"
print(txt.format("aligned"))

txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

txt = "We have {:d} chickens."
print(txt.format(0b101))

txt = "The octal version of {0} is {0:o}"
print(txt.format(10))

txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(15))

txt = "You scored {:%}"
print(txt.format(0.25))

txt = "You scored {:.0%}"
print(txt.format(0.25))

# String Interpolation / f-Strings (Python 3.6+)
print("f-Strings".center(100,"-"))
name = "python"
print(f'Hello, {name}!')

a = 10
b = 3
print(f"10 ** 3 = {a**b}")

# Template Strings :- It’s a simpler and less powerful mechanism
print("Template Strings".center(100,"-"))
from string import Template
a = "money"
b = "dollar"
my_string = Template("We can put ${a} with $b prefix and use them later, creating a template")
print(my_string.safe_substitute(a=a)) # $a is equal to ${a}
print(my_string.substitute(a=a,b=b))

coord = [3,4]
print('X: {0[0]};  Y: {0[1]}'.format(coord))

# format also supports binary numbers
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(10))
# with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(10))
print('{:,}'.format(1234567890))

