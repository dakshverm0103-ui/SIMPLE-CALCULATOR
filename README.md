🧮 Simple Python Calculator
📋 Description

This is a simple command-line calculator written in Python.
It allows the user to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

🚀 How It Works

The program asks the user to input two numbers.

Then it prompts the user to choose an operation (+, -, *, /).

Based on the user’s choice, the corresponding operation is performed and the result is displayed.

If the user enters an invalid operator, the program prints "Invalid choice".

💻 Code Example
# Simple Calculator Program

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
choice = input("Enter your choice (+, -, *, /): ")

if choice == "+":
    print(a + b)
elif choice == "-":
    print(a - b)
elif choice == "*":
    print(a * b)
elif choice == "/":
    print(a / b)
else:
    print("Invalid choice")

🧠 Example Output
Enter the first number: 10
Enter the second number: 5
Enter your choice (+, -, *, /): *
50

⚠️ Notes

Division by zero will raise an error.

Inputs should be valid numbers (integers).

You can easily modify this program to handle floating-point numbers by changing int() to float().

🏁 Author

Created by [DAKSH VERMA] — a simple example of Python control flow and user inpu
