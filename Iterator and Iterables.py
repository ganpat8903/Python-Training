a_list = [1, 2, 3, 4, 5, 6]
for item in a_list:
    print(item, end=' ')
    
# 1. The loop will get the iterator object of the list as list in python implements __iter__ method.
# 2. Then __next__ method will be called on that iterator object and it returns the next element of the list.
# 3. This goes on until all the elements of the list are retrieved.
# 4. When there are no more elements left __next__ method will raise StopIteration exception and loop terminates.
print()
# if we try to implement above steps without using for loop.
iterator = iter(a_list)
while True:
    try:
        print(next(iterator), end=' ')
    except StopIteration:
        break
print()
a=iter([10,20])
# print(a[0])  # error: 'list_iterator object is not subscriptable
# print(a.append(30)) # error: 'list_iterator' object has no attribute
print(type(a))
print(next(a))
print(next(a))
# print(next(a)) #  raise StopIteration exception 

d=iter({"name":"ganpat","salary":3000})
print(type(d))
print(next(d))
print(next(d))

s=iter({"a","b",1,2,1})
print(type(s))
print(next(s))

t=(1,2,3,"abc").__iter__()
print(type(t))
print(t)
print(next(t))
print(next(t))
print(t.__next__())
print(next(t))

# print(len(t)) # has no len() in iterator

numbers_iter = iter([1, 2, 3, 4, 5, 6])
for number in numbers_iter:
    if number == 4:
        break
    print(number) # 1 2 3
    
print(next(numbers_iter)) # 5
print(next(numbers_iter)) # 6
# You can also pass a second and optional argument to next(). 
# The argument is called default and allows you to provide a default value that’ll be returned 
# when the target iterator raises the StopIteration exception. 
print(next(numbers_iter,False)) 
