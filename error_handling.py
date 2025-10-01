#!/usr/bin/env python3
"""
Error handling in Python is crucial for building robust applications. This script demonstrates how to handle exceptions, including custom exceptions, and how to use the `logging` module for error reporting.
"""

def divide_numbers():
    """
    Example 1: Handling Division by zero
    """
    print("Division Calculator")
    try:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        result = num1 / num2
        print(f"Result is: {num1} / {num2} = {result}")
    except ZeroDivisionError as ex:
        print(f"Error: {num1} / 0 is not allowed")
    except ValueError as ex:
        print(f"Error: Invalid input. please enter a valid number")
    except Exception as ex:
        print(f"An unexpected error occured: {ex}")


def access_list_item():
    """ Example 2: Handling List index errors"""
    print("List Access demo")
    my_list = ["Apple", "Mango", "Banana" , "Orange"]
    print(f"Available Items: {my_list}")

    try:
        index = int(input("enter the index to access: "))
        item = my_list[index]
        print(f"Item at index {index} is : {item}")
    except IndexError:
        print("Error: Index out of range! please use indexes [0-3]")
    except ValueError:
        print("Error: Please enter a valid integer index.")

def read_file():
    """ Example 3: Handling File operations errors"""
    print("File Reading Demo")
    filename = input("Enter a file name to read: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File Content: {content}")
    except FileNotFoundError:
        print(f"file {filename} not found. Please check the file name and try again.")
    except PermissionError:
        print(f"Error: No Permission to read the file {filename}.")
    except Exception as e:
        print(f"Error reading file {filename}: {e}")

def convert_string_to_int():
    """Example 4: Using try-except with else and finally"""
    print("String to Integer converter")
    user_input = input("Enter a number: ")

    try:
        number = int(user_input)
        print(f"Converted number: {number}")
    except ValueError:
        print(f"Error: {user_input} is not a valid integer.")
        number = None
    else:
        # This runs only if no exception occurs
        print(f"Successfully converted {user_input} to {number}.")
        print(f"Double the number: {number * 2}")
    finally:
        # this always runs, regardless of excetions
        print("Conversion attempt completed.")

def age_validator():
    """Example 5: Custom Exception for Age Validation with try-except"""
    print("Age Validator")

    try:
        age = int(input("Enter your age: "))

        if age < 0 :
            raise ValueError("Age cannot be Negative")
        elif age > 150:
            raise ValueError("Age seems unrealistic")
        print(f"Your age {age} is valid. Thank you!")

        if age < 13 :
            category = "Child"
        elif age < 20:
            category = "Teenager"
        elif age <60:
            category = "Adult"
        else:
            category = "Senior Citizen"
        print(f"You are classified as {category}.")

    except ValueError as ex:
        if "invalid literal" in str(ex):
            print("Please enter a valid number")
        else:
            print(f"Error: {ex}")

def main():
    while True:
        print("-" * 50)
        print("Choose an example to run")
        print("1. Division Calculator")
        print("2. List Access Demo")
        print("3. File Reading Demo")
        print("4. String to Integer Converter")
        print("5. Age Validator")
        print("6. Exit")

        try:
            choice = input("Enter your choice (1-6):")
            print(f"You entered {choice}\n")
            if choice == '1':
                divide_numbers()
                continue
            if choice == '2':
                access_list_item()
                continue
            if choice == '3':
                read_file()
                continue
            if choice == '4':
                convert_string_to_int()
                continue
            if choice == '5':
                age_validator()
                continue
            if choice == '6':
                print("Thanks for participating. Goodbye!")
                break
            else:
                print("Invalid choice, please enter a valid choice")
    
        except KeyboardInterrupt:
            print("\n\n Program interrupted by the user, GoodBye!")
            break
        except Exception as ex:
            print(f"Unexpected error occured: {ex}")
if __name__ == "__main__":
    main()
    # Note: This script is a simple demonstration of error handling. In a production environment, you would typically use logging instead of print statements.
    # For example, you could replace print statements with logging like this:
    # import logging
    # logging.basicConfig(level=logging.ERROR)
    # logging.error(f"Error: {num1} / 0 is not allowed {ex}")
    # This way, you can easily control the logging level and redirect logs to files or other outputs.
    # Additionally, you can create custom exceptions for more specific error handling.
    # Custom exceptions can be defined by subclassing the built-in Exception class.
