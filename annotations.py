# to check data type are right or not install mypy
# to run mypy: python -m mypy rough.py
import math

def headline(text: str, align: bool = True) -> str:
    if align:
        # The title() method returns a string where the first character in every word is upper case.
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")# 50 is total length text + o  
print(headline("python type checking"))
print(headline("python type checking", align=False))

def circumference(radius: float) -> float:
    return 2 * math.pi * radius
print(circumference(1.23))
print(circumference.__annotations__)
# When running the code, you can also inspect the annotations.
# They are stored in a special .__annotations__ attribute on the function.

p: int = 3
pi = 3  # type: int
# p and pi both are same we can write type in comment also
def circle(radius: float) -> float:
    return 2 * p * radius**2
print(circle(2.5))
print(circle.__annotations__)
print(__annotations__)

def message(text, width=80, fill_char="-"):
    # type: (str, int, str) -> str 
    #  this above comment works for annotations
    return f" {text.title()} ".center(width, fill_char)
print(message("type comments work", width=40))

names: list = ["Guido", "Jukka", "Ivan"]
version: tuple = (3, 7, 1)
options: dict = {"centered": False, "capitalize": True}
''' What will be the types of names[2], version[0], and options["centered"]? 
    In this concrete case you can see that they are str, int, and bool, respectively.'''
from typing import Dict, List, Tuple, Sequence, Any
names1: List[str] = ["Guido", "Jukka", "Ivan"]
version1: Tuple[int, int, int] = (3, 7, 1)
options1: Dict[str, bool] = {"centered": False, "capitalize": True}
# if you don't know whether it is list or tuple then you can use Sequence after import typing.
seq: Sequence[str] = ("Guido", "Jukka", "Ivan")
s: Any={'byy'} # any type it can take
# Dict[str, Any]

# If there is no return in function then it is None
def play(player_name: str) -> None:
    print(f"{player_name} plays")
play("Filip")
