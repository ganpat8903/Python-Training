print(int(False))
print(float(True))
print(True+True+False)
print(issubclass(bool,int))  # True
print(issubclass(int,bool)) # False
print(issubclass(int,int)) # True
print(issubclass(bool,bool)) # True
print(issubclass(int,float)) # False
print(issubclass(float,int)) # False

def double(number: int) -> int:
    return number * 2
print(double(True))  # Passing in bool instead of int
