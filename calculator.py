from typing import Union, Optional, TypeVar, Callable
from math import sqrt, pow
from decimal import Decimal, InvalidOperation

Number = TypeVar('Number', int, float, Decimal)
Result = Union[Number, None]

class CalculatorError(Exception):
    """Custom exception for calculator operations"""
    pass

class Calculator:
    """
    Advanced calculator implementation with type safety and error handling.
    Supports basic arithmetic, power operations, and square root.
    """
    
    @staticmethod
    def validate_numbers(*args: Number) -> None:
        """Validate that all arguments are numeric types"""
        for arg in args:
            if not isinstance(arg, (int, float, Decimal)):
                raise TypeError(f"Expected numeric type, got {type(arg)}")

    @staticmethod
    def safe_operation(operation: Callable[..., Result]) -> Callable[..., Result]:
        """Decorator for safe operation execution with error handling"""
        def wrapper(*args: Number, **kwargs) -> Result:
            try:
                Calculator.validate_numbers(*args)
                return operation(*args, **kwargs)
            except (TypeError, ValueError, ZeroDivisionError, InvalidOperation) as e:
                raise CalculatorError(f"Operation failed: {str(e)}")
        return wrapper

    @staticmethod
    @safe_operation
    def add(x: Number, y: Number) -> Number:
        """Add two numbers"""
        return x + y

    @staticmethod
    @safe_operation
    def subtract(x: Number, y: Number) -> Number:
        """Subtract y from x"""
        return x - y

    @staticmethod
    @safe_operation
    def multiply(x: Number, y: Number) -> Number:
        """Multiply two numbers"""
        return x * y

    @staticmethod
    @safe_operation
    def divide(x: Number, y: Number) -> Optional[Number]:
        """
        Safely divide x by y
        Returns None if division by zero is attempted
        """
        if isinstance(y, (int, float)) and y == 0:
            return None
        if isinstance(y, Decimal) and y == Decimal('0'):
            return None
        return x / y

    @staticmethod
    @safe_operation
    def power(x: Number, y: Number) -> Number:
        """Calculate x raised to the power of y"""
        return pow(x, y)

    @staticmethod
    @safe_operation
    def square_root(x: Number) -> Optional[Number]:
        """
        Calculate the square root of x
        Returns None for negative numbers
        """
        if x < 0:
            return None
        return sqrt(x)

    @staticmethod
    def to_decimal(value: Union[str, Number]) -> Decimal:
        """Convert a value to Decimal for precise arithmetic"""
        try:
            return Decimal(str(value))
        except (InvalidOperation, ValueError) as e:
            raise CalculatorError(f"Cannot convert to Decimal: {str(e)}")

# Example usage:
if __name__ == "__main__":
    try:
        # Basic arithmetic
        print(f"Addition: {Calculator.add(5, 3)}")
        print(f"Division: {Calculator.divide(10, 2)}")
        
        # Precise decimal arithmetic
        x = Calculator.to_decimal("3.14159265359")
        y = Calculator.to_decimal("2.71828182846")
        print(f"Precise addition: {Calculator.add(x, y)}")
        
        # Advanced operations
        print(f"Power: {Calculator.power(2, 3)}")
        print(f"Square root: {Calculator.square_root(16)}")
        
    except CalculatorError as e:
        print(f"Error: {e}") 