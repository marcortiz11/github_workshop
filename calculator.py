def add(x: int, y: int) -> int:
    """Add two integer values"""
    return x + y

def div(x, y) -> float:
    """Divide two integer values"""
    if (y == 0):
        raise ValueError("Division by zero")
    else:
        return x / y