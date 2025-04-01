def add_us(a, b):
    c = a + b
    return c

a = float(input("Enter a number: "))
b = float(input("Enter second number: "))
print(add_us(a, b))

def no_return():
    print("Hello!")
    
print(no_return()) # return None

def my_args_are_must(first, second, third):
    print("I got all of them!")
    print(first)
    print(second)
    print(third)
    
my_args_are_must("asdf", 12, [1, 2, 3])
# my_args_are_must(1, 3) # TypeError: my_args_are_must() missing 1 required positional argument: 'third'

def call_with_names(first, second, third):
    print(f"first: {first}")
    print(f"second: {second}")
    print(f"third: {third}")
    
call_with_names(second=2, first=1, third=3) # when you call using arg names order does not matter.
# call_with_names(first=1, second=2, 3) # SyntaxError: positional argument follows keyword argument.
call_with_names(1, third=3, second=2) # keyword arguments must come after positional arguments.

def i_have_defaults(first, second=2, third=3, zero=0):  # default arguments can not come before non-defaults
    print("Default argument".center(100,"-"))
    print(f"first: {first}")
    print(f"second: {second}")
    print(f"third: {third}")
    print(f"zero: {zero}\n")
    
i_have_defaults(first=1)
i_have_defaults(1, zero=1)
i_have_defaults(1, zero=-1)

# def variable_length_args(*args,b): error *args must be last
def variable_length_args(a,*args): 
    print(f"type of args: {type(args)}")
    print(f"type of args: {type(a)}")
    print(a)
    print(args)
        
variable_length_args('abc', 1, (2, 3,), [2, 'b'], 2.14)

def variable_length_kwargs(third,**kwargs):
    print(f"\ntype of kwargs: {type(kwargs)}")
    print(type(third))
    print(third)
    print(kwargs)
        
variable_length_kwargs(first='a', second=1, third=(2, 3,), fourth=[2, 'b'], fifth=2.14)

get_my_square = lambda x : x**2
print(f"square of 0 is: {get_my_square(0)}")
print(f"square of 1 is: {get_my_square(1)}")
print(f"square of 2 is: {get_my_square(2)}")
print(f"square of 3 is: {get_my_square(3)}")
print(f"square of 4 is: {get_my_square(4)}")
print(f"square of 5 is: {get_my_square(5)}")

pairs = [(11, 'one'), (22, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(f"sorted pairs: {pairs}")

print(type(variable_length_kwargs))

def f(a,b,/,c,*,d,e):
    print(a,b,c,d,e)
f(1,2,c=3,d=4,e=5)

def f(x):
    if x < 0:
        return # exit from function
    if x > 100:
        return
    print(x)
f(-1)
f(1)
f(200)

def fun(a, b, c):
    print(F'a = {a}')
    print(F'b = {b}')
    print(F'c = {c}')
d = {'a': 'foo', 'b': 25, 'c': 'qux'}
fun(**d)
