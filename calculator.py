def add(x: int, y: int) -> int:
    """Add two integer values"""
    return x + y

def div(x, y) -> float:
    """Divide two integer values"""
    assert y != 0, "Cannot divide by zero"
    return x / y
