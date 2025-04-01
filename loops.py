# for loop
# Iterate over a list
print("list".center(100,"-"))
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in a_list:
    print(num, end=' ')
    
# Iterate over a tuple
print("\n"+"tuple".center(100,"-"))
a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for num in a_tuple:
    print(num, end=' ')
    
## Iterate over a set
print("\n"+"set".center(100,"-"))
a_set = {-11, 2, 3, 4, 15, 6, 7, 8, 9, 10,0}
print(a_set)
for num in a_set:
    print(num, end=' ')

## Iterate over a dict
print("\n"+"dict".center(100,"-"))
a_dict = {"a":1, "b":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10}
print("Keys: ")

for key in a_dict:
    print(key, end=' ')
print('\n\nValues: ')

for value in a_dict.values():
    print(value, end=' ')
    
for key, value in a_dict.items():
    print(f"key: {key}, value: {value}")
    
# Iterate over a range
print("\n"+"range".center(100,"-"))
print("0 to 99")
for num in range(100):
    print(num, end=' ') # this will print from 0 to 99

print("\n\n1 to 100")
for num in range(1, 101):
    print(num, end=' ') # this will print from 1 to 100
    
# specifying step argument
print("\n\nEven numbers in 0 to -101")
for num in range(0, -101, -2):
    print(num, end=' ')
    
# while loop
# Iterate over a list
print("\n"+"list".center(100,"-"))
a_list = list(range(10))
index = 0
while index < len(a_list):
    print(a_list[index], end=' ')
    index += 1
    
# Iterate over a tuple
print("\n"+"tuple".center(100,"-"))
a_tuple = tuple(range(20,30))
index = 0
while index < len(a_tuple):
    print(a_tuple[index], end=' ')
    index += 1

# Iterate over a set
print("\n"+"set".center(100,"-"))
a_set = set(range(-20,-10))
index = 0
print(a_set)
print("we cannot find index of set because it is unordered")
# while index < len(a_set):
#     print(a_set[index], end=' ') #we cannot find index of set because it is unordered
#     index += 1

# Iterate over a dict
print("\n"+"dict".center(100,"-"))
a_dict = {"a":1, "b":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10}
print("we cannot do dict from while loop ")
# we cannot do dict from while loop 

# pass: does nothing 
print("\n"+"pass".center(100,"-"))
def f(arg):
    pass    # a function that does nothing (yet)

class C: 
    pass       # a class with no methods (yet)

for i in range(10):
    if i%2 == 0:
        print(i, end=' ')
    else:
        pass # do nothing if number is odd
    
# break: Break the loop and exits the code block.
print("\n"+"break".center(100,"-"))
a_list = list(range(100))
for num in a_list:
    if num > 10:
        break
    print(num, end=' ')
    
# continue: Skips the next part of loop and continues to next iteration.
print("\n"+"continue".center(100,"-"))
a_list = list(range(100))
for num in a_list:
    if num%5 != 0:
        continue
    print(num, end=' ')
    
# else with for loop
print("\n"+"else with for loop".center(100,"-"))
# When the condition becomes false then go to else
# But not when the loop is terminated by a break statement
is_prime = 37
for num in range(2, is_prime//2):
    if is_prime%num == 0:
        print(f"{is_prime} has a factor {num} * {is_prime/num}")
        break
else:
    print(f"{is_prime} is a prime number")

# else with while loop
print("\n"+"else with while loop".center(100,"-"))
is_prime = 37
num = 2
limit = is_prime//2

while num<limit:
    if is_prime%num == 0:
        print(f"{is_prime} has a factor {num} * {is_prime/num}")
        break
    num += 1
else:
    print(f"{is_prime} is a prime number")
    
# breaking nested loops
print("\n"+"breaking nested loops".center(100,"-"))
# Using a flag to notify outer loop. 
break_outer = False
while True:
    for num in range(100):
        if num>10:
            break_outer = True
            break
        print(num, end=' ')
    if break_outer:
        break
    
# Raising an exception
print()
class GetOutOfLoop( Exception ):
    pass
while True:
    try:
        for num in range(100):
            if num>10:
                raise GetOutOfLoop
            print(num, end=' ')
    except GetOutOfLoop:
        break
    
print()   
def my_loops():
    while True:
        for num in range(100):
            if num>10:
                return "by"
            else:
                print(num, end=' ')
print(my_loops())

while True: 
    for num in range(100):
        if num > 10:
            break
        else:
            print(num, end=' ')
    else:
        continue
    break

print()
def my_loops():
    while True:
        for num in range(20,100):
            if num > 30:
                yield False
            else:
                yield num

for item in my_loops():
    if item is not False:
        print(item, end=' ')
    else:
        break
    
# Python program to display the Fibonacci sequence using recursion
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10
if nterms <= 0:
    print("\nPlese enter a positive integer")
else:
    print("\nFibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i),end=" ")
 
print()   
def myFunc():
  yield "Hello"
  yield 51
  yield "Good Bye"
  
x = myFunc()
  
# for z in x:
#   print(z)
print(next(x))
print(next(x))
print(next(x))

for i in range(5):
    print(i)
    i=10
