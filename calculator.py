def add(x, y):
    return x + y

def div(x, y):
    if (y == 0):
        raise ValueError("Division by zero")
    else:
        return x / y
