from itertools import chain

numbers = [1, 2, 3]
characters = {'a', 'b', 'c'}


chained_iterables = chain(numbers, characters)  # It combines the sequences.
print(f"TYPE: {type(chained_iterables)}")

print(f"Calling next: {next(chained_iterables)}")
print(f"Calling next: {next(chained_iterables)}")
print(f"Calling next: {next(chained_iterables)}")
print(f"Calling next: {next(chained_iterables)}")
print(f"Calling next: {next(chained_iterables)}")
print(f"Calling next: {next(chained_iterables)}")

for i in chain(numbers, characters):
    print(i, end=' ')

a=[1,2,3,4,5]
b=("a","b","c")
print(list(zip(a,b)))

from itertools import zip_longest
print(list(zip_longest(a,b, fillvalue="Noo"))) # by default fillvalue is None

a=[[1,2],[3,4]]
b=chain(a)
print(list(b)) 

c=chain.from_iterable(a)
print(list(c))

from itertools import tee
a,b,c=tee("python",3) # by default 2
print(next(a))
print(next(b))

a=[1,2,3]
def fun(x):
    return 2*x
m=map(fun,a)
print(list(m))

from itertools import starmap
m=starmap(pow, [(2,5), (3,2), (10,3)])
print(list(m))

from itertools import count
counter=count(5,5) # by default 0 and second parameter is for step
print(next(counter))
print(next(counter))
print(next(counter))

from itertools import cycle
cyc=cycle([1,2,3])
print(next(cyc))
print(next(cyc))
print(next(cyc))
print(next(cyc))

from itertools import repeat
rep=repeat([11,12],2) # second parameter is for how many times repeat by default unlimited
print(next(rep))
print(next(rep))

from itertools import dropwhile
def check(x):
    return x<0
a=dropwhile(check,[-2,-1,1,2,-3]) #After the condition is false the first time, all of the remaining items in the input are returned.
print(list(a))

from itertools import takewhile #The opposite of dropwhile().
a=takewhile(check,[-2,-1,1,2,-3]) #After the condition is false the first time, all of the remaining items in the input are not returned.
print(list(a))
# print(dir(list)) to check methods

a=[-2,-1,1,2,-3]
def fun_filter(x):
    return x<0
f=filter(fun_filter,a)
print(list(f))

from itertools import filterfalse
ff=filterfalse(fun_filter,a)
print(list(ff))

from itertools import compress
a=compress([1,2,3,4],[10,"",True,0])
print(list(a))

from itertools import groupby
a=[("A","ant"),("A","ball"),("A","apple"),("B","banana")]
def group_by(x):
    return x[0]

for key,group in groupby(a,group_by):
    print(key,":")
    for thing in group:
        print(thing[1])

from itertools import accumulate
import operator
numbers = [1, 1, 2, 3, 4, 5, 6, 7]
characters = ['a', 'b', 'c', 'd', 'e']
print(list(accumulate(numbers))) # by default operator is add
print(list(accumulate(characters)))
print(list(accumulate(numbers,operator.mul))) 

from itertools import product
numbers = [0, 1, 2]
characters = ['a', 'b', 'c', 'd', 'e']

for num in product(numbers, characters):
    print(num, end=' ')

print("\n\nproduct with self\n")    

for num in product(numbers,repeat=2):
    print(num, end=' ')

from itertools import permutations
# order matter i.e. ('a', 'b') and ('b', 'a') are different
print('All permutations:\n')
print(list(permutations('abc')))

print("\nLimit length to 2:\n")
print(list(permutations('abc', r=2)))

from itertools import combinations,combinations_with_replacement
# order does not matter i.e. ('a', 'b') and ('b', 'a') are same
print('All combinations:\n')
print(list(combinations('abc',r=3))) # length is required 

print("\nLimit length to 2:\n")
print(list(combinations('abc', r=2)))

print('Unique pairs:\n') # include repeated elements
print(list(combinations_with_replacement('abc', r=2)))
