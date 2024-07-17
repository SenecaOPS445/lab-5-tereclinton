#!/usr/bin/env python3
# Author ID: 119911220

def add(number1, number2):
    # Attempt to add two numbers; if an error occurs, return a custom error message.
    try:
        # Try to convert both inputs to float for addition to handle strings that represent numbers.
        return float(number1) + float(number2)
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()  # This will include newline characters
    except Exception:
        return 'error: could not read file'  # Keep the error message simple


    

if __name__ == '__main__':
    print(add(10, 5))  # Expected to work, prints 15
    print(add('10', 5))  # Expected to work, prints 15
    print(add('abc', 5))  # Will cause an exception, prints error message

    print(read_file('seneca2.txt'))  # Assuming seneca2.txt exists and is readable
    print(read_file('file10000.txt'))  # Expected to fail as file likely doesn't exist
