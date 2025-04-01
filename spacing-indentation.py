year=2000
month=6
minute=40
#  backslash \ is used to write in next line 
if 1900 < year < 2100 and \
1 <= month <= 12  \
            and 0 <= minute < 60:
        print("Done")
        
if True:
    print("Indentation is proper.")
    
# escape sequences
print("Hello! How are you? \n newline.")
print("Hello! How are you? \' Single quote.")
print("Hello! How are you? \" Double quote.")
print("Hello! How are you? \t tab.")

# formatted string or f-string
name="Ganpat"
print(f"hello {name}") # f and F both are same
print(f"hello {name!r}.") # representation of object repr()
print(f"hello {repr(name)}") # !r and repr() both are same
