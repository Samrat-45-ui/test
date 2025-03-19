import argparse
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

def calculate(operation, num1, num2):
    """Performs basic arithmetic operations."""
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Unsupported operation.")

def main():
    parser = argparse.ArgumentParser(description="Simple yet advanced calculator.")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform.")
    parser.add_argument("num1", type=float, help="First number.")
    parser.add_argument("num2", type=float, help="Second number.")
    args = parser.parse_args()

    try:
        result = calculate(args.operation, args.num1, args.num2)
        logging.info(f"Operation: {args.operation}, Numbers: {args.num1}, {args.num2}, Result: {result}")
        print(f"The result is: {result}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"Error: {e}")


main()