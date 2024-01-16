import math

def add(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print("Error: Cannot add a string and a number.")
        return None
    except ArithmeticError:
        print("Error: Cannot add no numbers.")
        return None
    
def substract(num1, num2):
    return num1 - num2
    
def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    
def power(x, y):
    return math.pow(x, y)

def square_root(x):
    try:
        return math.sqrt(x)
    except ValueError:
        return "Error: Cannot calculate square root of a negative number."

def logarithm(x, base):
    try:
        return math.log(x, base)
    except ValueError:
        return "Error: Cannot calculate logarithm of a negative number."

def factorial(x):
    try:
        return math.factorial(x)
    except ValueError:
        return "Error: Cannot calculate factorial of a negative number."

def menu():
    menu = [ "Select an operation:",
        "1. Addition",
        "2. Subtraction",
        "3. Multiplication",
        "4. Division",
        "5. Power",
        "6. Square root",
        "7. Logarithm",
        "8. Factorial",
        "9. Reset",
        "0. Exit"
    ]

    print("----------------Menu----------------")
    for item in menu:
        print(item)
    print("------------------------------------")

def main():
    result = float(input("Enter first number: "))
    menu()
    while True:
        choise = input("Введите операцию: ")
            
        if choise == "6":
            result = square_root(result)
        elif choise == "8":
            result = factorial(int(result))
        elif choise == "7":
            base = float(input("Enter the base: "))
            result = logarithm(result, base)
        else:
            if choise != "0":
                s_number = float(input("Enter second number: "))

            if choise == "1":
                result = add(result, s_number)
            elif choise == "2":
                result = substract(result, s_number)
            elif choise == "3":
                result = multiply(result, s_number)
            elif choise == "4":
                result = divide(result, s_number)
            elif choise == "5":
                result = power(result, s_number)
            elif choise == "9":
                result = 0
            elif choise == "0":
                print("Exiting calculator!")
                break
            else:
                raise ValueError("Неверный оператор!")

        print("Result: ", result)


            

if __name__ in "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Pressed Ctrl+C...")
    finally:
        print("Calculator exited...")