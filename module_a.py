print(f"out side a's display method")

def show():
    import module_b
    module_b.display()

def display():
    print(f"in side a's display method")

show()