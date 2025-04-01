print(f"out side b's display method")

def show():
    import module_a
    module_a.display()

def display():
    print(f"in side b's display method")

show()