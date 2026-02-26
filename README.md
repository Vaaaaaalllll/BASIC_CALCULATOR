<!-- WARNING: template code, may need edits -->
# Basic Calculator

A simple Python calculator that performs addition and subtraction operations.

## Features

- Addition of numbers
- Subtraction of numbers
- Command-line interface
- Input validation
- Error handling

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd BASIC_CALCULATOR

# No external dependencies required - uses Python standard library only
```

## Usage

```bash
# Run the calculator
python src/main.py
```

### Example

```
Welcome to Basic Calculator!
Select operation:
1. Add
2. Subtract
3. Exit

Enter choice (1/2/3): 1
Enter first number: 10
Enter second number: 5
Result: 10 + 5 = 15
```

## Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=src
```

## Project Structure

```
BASIC_CALCULATOR/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── calculator.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_utils.py
├── docs/
│   └── API.md
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## License

MIT License