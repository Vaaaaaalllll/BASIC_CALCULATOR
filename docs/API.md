<!-- WARNING: template code, may need edits -->
# Basic Calculator API Documentation

## Calculator Class

### `Calculator.add(a, b)`

Adds two numbers together.

**Parameters:**
- `a` (int | float): First number
- `b` (int | float): Second number

**Returns:**
- (int | float): Sum of a and b

**Examples:**
```python
from calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)  # Returns 8
result = calc.add(2.5, 1.5)  # Returns 4.0
```

---

### `Calculator.subtract(a, b)`

Subtracts the second number from the first number.

**Parameters:**
- `a` (int | float): First number (minuend)
- `b` (int | float): Second number (subtrahend)

**Returns:**
- (int | float): Difference of a and b

**Examples:**
```python
from calculator import Calculator

calc = Calculator()
result = calc.subtract(10, 3)  # Returns 7
result = calc.subtract(5, 10)  # Returns -5
```

---

## Utility Functions

### `get_number_input(prompt)`

Prompts user for numeric input with validation.

**Parameters:**
- `prompt` (str): Message to display to user

**Returns:**
- (float | None): Parsed number or None if invalid

**Examples:**
```python
from utils import get_number_input

num = get_number_input("Enter a number: ")
if num is not None:
    print(f"You entered: {num}")
```

---

### `get_operation_choice()`

Prompts user to select an operation.

**Returns:**
- (str | None): Choice ('1', '2', or '3') or None if invalid

**Examples:**
```python
from utils import get_operation_choice

choice = get_operation_choice()
if choice == '1':
    # Perform addition
    pass
```

---

### `format_result(num1, num2, operation, result)`

Formats a calculation result as a readable string.

**Parameters:**
- `num1` (int | float): First number
- `num2` (int | float): Second number
- `operation` (str): Operation symbol ('+' or '-')
- `result` (int | float): Calculation result

**Returns:**
- (str): Formatted result string

**Examples:**
```python
from utils import format_result

output = format_result(10, 5, '+', 15)
print(output)  # "Result: 10 + 5 = 15"
```

---

## Error Handling

The calculator includes robust error handling:

- **Invalid numeric input**: Returns `None` and displays error message
- **Invalid operation choice**: Returns `None` and prompts for valid input
- **Type errors**: Handled by Python's type system and input validation

## Usage Example

```python
from calculator import Calculator
from utils import get_number_input, format_result

calc = Calculator()

# Get user input
num1 = get_number_input("Enter first number: ")
num2 = get_number_input("Enter second number: ")

if num1 is not None and num2 is not None:
    # Perform calculation
    result = calc.add(num1, num2)
    
    # Display result
    print(format_result(num1, num2, '+', result))
```
