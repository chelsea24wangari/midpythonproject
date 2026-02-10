# Create a simple calculator program
from random import choice

def add(a,b):
    result = a + b

def subtract (a,b):
    result = a - b

def multiply (a,b):
    result = a * b

def divide (a,b):
    result = a / b




def calculator():
    print("Calculator (+)")
    print("Choose an Operation (+)")
    print("Add (+)")
    print("Subtract (-)")
    print("Multiply (*)")
    print("Divide (/)")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("Result:", (num1 + num2))
elif choice == "2":
    print("Result:", (num1 - num2))
elif choice == "3":
    print("Result:", multiply(num1 * num2))
elif choice == "4":
    print("Result:", divide(num1 / num2))
else:
    print("Invalid choice")



