# without exception handling

def division(a, b):
    print("About to start calculation")
    res = a / b
    print(f"Result = {res}")
    print("Calculation ended")

print("Program is starting")
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
division(n1, n2)
print("Program is ending")

_______________________________________________________________________________

# with exception handling

def div(a, b):
    print("About to start calculation")
    try:
        res = a / b
        print(f"Result = {res}")
    except ZeroDivisionError:  # Handles division by zero
        print("Division by zero is not allowed")

print("Program is starting")
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
div(n1, n2)
print("Program is ending")
_______________________________________________________________________________
# Try except finally

def calculation(a, b):
    print("About to start calculation")
    try:
        res = a / b
    except ZeroDivisionError:  # Handles division by zero
        print("Division by zero is not allowed")
    else:  # Executes only if no exception occurs
        print(f"Result = {res}")
    finally:  # Executes regardless of whether an exception occurs
        print("Program about to exit")

print("Program is starting")
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
calculation(n1, n2)
print("Program is ending")
_______________________________________________________________________________
# Multiple exception handling

def calc(a, b):
    print("About to start calculation")
    try:
        div = a / b
        print(f"Division = {div}")

        add = a + c
        print(f"Addition = {add}")

    except ZeroDivisionError: # First (Specific)exception
        print("Division by zero is not allowed")

    except NameError: # Second (Specific) exception
        print("Variable not defined")

    except Exception: # default exception
        print("unknown error")

    else:
        print("Both operations were successful!")

    finally:
        print("Program about to exit")

print("Program is starting")
try:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))

    calc(n1, n2)
except ValueError:
    print("Error: Please enter valid integers.")
finally:
    print("Program is ending")


# creating user Excecption
class AgeError(Exception):
    pass

def validate(age):
    if age >= 18:
        print("Eligible for voting!")
    else:
        raise AgeError("Age must be >= 18")

# Main Program
try:
    age = int(input("Enter your age: "))
    validate(age)
except AgeError as e:
    print(f"Error: {e}")

except ValueError:
    print("Error: Please enter a valid integer for age.")

finally:
  print("Exceuted...")

try:
    n1= int(input("Enter a number: "))
    n2= int(input("Enter a number: "))

    result = n1 / n2
    print(result)
except (ZeroDivisionError, ValueError) as e:
    print(f"Error: {e}")

print("hello world")

x = 5

print(x)

for i in range(10):
  print(i)
