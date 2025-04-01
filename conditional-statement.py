if True:
    print("True statement")
if False:
    print("False statement")
    
if True:
    print("If is true.")
else:
    print("byyyy")

if False:
    print("If is False.")
else:
    print("good bye")
    
if False:
    print("I am if with False condition.")
elif True:
    print("I am elif with True condition and prior False if.")
else:
    print("I am else with prior True elif.")

if True:
    print("I am if with True condition.")
elif True:
    print("I am elif with True condition.")
else:
    print("I am else with prior True elif")

if False:
    print("I am if with False condition.")
elif False:
    print("I am true elif with True condition.")
else:
    print("I am else with prior False elif.")
    
a = 10
b = 12
c = 2
# largest among the three
if b < a and c < a:
    print(f"{a} is largest number")
elif b > c:
    print(f"{b} is largest number")
else:
    print(f"{c} is largest number")


# finding the middle number:
if b < a < c or c < a < b:           
    print(f"{a} is the middle number")
elif a < b < c or c < b < a:
    print(f"{b} is the middle number")
else:
    print(f"{c} is the middle number")

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if a in a_list:
    print(f"{a} is in the list")
else:
    print(f"{a} is not in the list")

if b in a_list:
    print(f"{b} is in the list")
else:
    print(f"{b} is not in the list")


if c in a_list:
    print(f"{c} is in the list")
else:
    print(f"{c} is not in the list")


some_string = "Welcome to the world of Python!"
sub_str = "to t"

if sub_str in some_string:
    print(f"'{sub_str}' is a sub string of '{some_string}'.")

some_dict = {"this": 1, "is": 2, "key": 3}

if 1 in some_dict:   # dict compares the keys instead of values
    print(f"{1} is in the dictionary")

if 2 in some_dict.values():  # to compare values use values() method
    print(f"{2} is in the dictionary")

a = 100
b = 100.0

if a == b:
    print("Value of a and b is same")
if a is b:
    print("a and b are same object")
a = "asdf"
b = "asdf"
print(id(a),id(b))
print(a is b)
a = "manali"
b = input()
print(id(a),id(b))
print(a is b)

for i in range(5):
    print(i)
    if i==3:
        continue
else:
    print("else",i)
    
    
i = 5
def f(arg=i):
    print(arg)
i = 6
f() # 5

a=1
match "1": 
    case "1" | 1:print("byy")
    case 2:print("good")
    case _:print("hello")    

# short-circuit operator
print("age" and None)   
print(None and "age")
print(None or "age")
print( "age" or None)
print( "age" and "name")
print( "age" or "name")
print(bool(""))
print(bool("age"))
a=(2,)
print(type(a))
pass