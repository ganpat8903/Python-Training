# The built-in function ord() converts a code point from its string form to an integer in the range 0 - 10FFFF
print(ord("A"))
# chr() converts an integer in the range 0 - 10FFFF to the corresponding length 1 string object.
print(chr(99))

x="string"
print(type(x)) # <class 'str'>

x=10
print(type(x)) # <class 'int'>

x=10.5
print(type(x)) # <class 'float'>

x=1+2j
y=2+4j
print(x+y) #(3+6j)
print(type(x)) # <class 'complex'>

x=True
print(type(x)) # <class 'bool'>

my_str = "This is a sequence"
print("length of the sequence is: {} {}".format(len(my_str),"length"))
print("Character at 7th position is: {}".format(my_str[6]))
# my_str[1]="b" we cannot change the value in string

a = "abcd"
b = "c"
print(a[2] is b[0])
for char in a:
    print(id(char))
print(id(a[2]))
print(id(b[0]))

# All of them are tuples
print("tuples".center(100,"-"))
a = 1, 2, 3
print(a)
b = (4, 5, 6)
print(b)
c = 1,
print(c)
d = ()
print(d)
e = tuple()
print(e)

# creating list
print("list".center(100,"-"))
a = list()
print(a)
a = []
print(a)
a = [1, 'x', 3, '1']
print(a)
a = [1]
print(a)

a = [1, 2, 0, 2]
print(a)
print(id(a))
a.append(3)
print(id(a))
print("After appending 3 to list: \n{}".format(a))

b = ['a', 'b', 'c']
a.extend(b)
print("Extending list with method: \n{}\n".format(a))
c = [True, False]
a = a + c
print("Extending list using + operator: \n{}\n".format(a))

# creating set
print("set".center(100,"-"))
a = set()
print("Type of a: {}".format(type(a)))
a = {'a', 1, 2, 3, '1', 1, 2, 3, 'a'}
print("Contents of a: {}".format(a))
# adding an item to set
a.add("added")
print("\nAfter adding an item: \n{}\n".format(a))

# updating set
a.update([1, 4, False])
print("After updating set: \n{}\n".format(a))

# remove an item from set
a.remove('added')
print("After removing an item from set: \n{}\n".format(a))

# discard an item from set
a.discard("added")
print("After discarding an item form set: \n{}\n".format(a))

# clearing the set
a.clear()
print("Set after being cleared: \n{}\n".format(a))

# frozenset 
print("frozenset".center(100,"-"))
a = frozenset([1, 2, 3, 4])
print(a)
# a.add(2) error

# creating a dict
print("dict".center(100,"-"))
a = dict()
print("a is: \n{}\n".format(a))

a = {}
print("a is: \n{}\n".format(a))

a = {0: 'something', 1: 'is', 2: 'not', 3:True, 'what?': 'maybe'}
print("a is: \n{}\n".format(a))

a = dict(one=1, two=2, three=3)
print("a is: \n{}\n".format(a))

a = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print("With ZIP a is: \n{}\n".format(a))

a = dict([('one', 1), ('two', 2), ('three', 3)])
print("a is: \n{}\n".format(a))

# listing the keys of dictionary
print("The keys in a are: \n{}\n".format(list(a)))
print("The keys in a are: \n{}\n".format(a.keys()))

# accessing items by key
print("Item with key 'one' is: \n{}\n".format(a['one']))  # this will raise KeyError if key is not present
print("Value with key 'one' is: \n{}\n".format(a.get('one'),"not found")) # this will return None if key is not present
print("Value with key 'on' is: \n{}\n".format(a.get('on', "Key not present"))) # you can also give default value to return if key is not found
print(a)

# changing value at a key
a['one'] = 'one'
print("dict after being changed: \n{}\n".format(a))

# pop a key and value
value = a.pop('two', "Key not present")  # if key is not there return default. If default not given raise keyerror
print("Popped value from dict is: \n{}\n".format(value))
print("Dict after popping value is: \n{}\n".format(a))

# popping last item from dict
key_value = a.popitem()  # return a tuple with key and value. if dict is empty raise keyerror
print("Popped last item is: \n{}\n".format(key_value))

print('hello', 'world', sep=None)
print('hello', 'world', sep=' & ')
print('hello', 'world')
print('Checking file integrity...',end='by')
print('The first sentence')
print('Mercury', 'Venus', 'Earth', sep=', ', end=', ')
print('Mars', 'Jupiter', 'Saturn', sep=', ', end=', ')
print('Uranus', 'Neptune', 'Pluto', sep=', ')