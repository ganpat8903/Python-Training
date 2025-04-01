squares = []

for num in range(1, 11):
    squares.append(num*num)

print(squares)

del squares

squares = [num*num for num in range(1, 11)]
print(squares)

# get squares of even numbers and cubes of odd numbers in a range.
squares_and_cubes = [i*i*i if i%2!=0 else i*i for i in range(1, 21)]
print(squares_and_cubes)

# find unique vowels from a sentence.
sentence = "Get me all the unique vowels man!"
vowels = "aeiou"
unique_vowels_in_sentence = {char for char in sentence if char in vowels}
print(unique_vowels_in_sentence)

# creat a dict out of list of numbers with number as a key and their square roots as value.
import math
squares = {num: f"{math.sqrt(num):.2f}" for num in range(1, 11)}
print(squares)

data=['fizzbuzz' if x % 3 == 0 and x % 5 == 0 
                else 'fizz' if x % 3 == 0 
                else 'buzz' if x % 5 == 0 
                else x 
                for x in range(20)]
print(data)

def transform(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    return number

def fizz_buzz2_comprehension():
    return [transform(number) for number in range(20)]
print(fizz_buzz2_comprehension())

multiplication = [{i * j for j in range(1, 6)} for i in range(2, 5)]
print(multiplication)