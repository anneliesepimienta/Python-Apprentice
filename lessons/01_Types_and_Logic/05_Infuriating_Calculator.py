"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Hide the window, hint: use the withdraw method
window = Tk()
window.withdraw()
num1 = input("Enter a number")
num2 = input("Enter another number")
opp = input("Would you like to add, subtract, multiply, or divide your 2 numbers.")  
if opp == "add":
    print("The sum of your numbers is " + str(int(num1) + int(num2)))
elif opp == "subtract":
    print("The difference of your numbers is " + str(int(num1) - int(num2)))
elif opp == "multiply":
    print("The product of your numbers is " + str(int(num1) * int(num2)))
# Ask the user for the math operation
elif opp == "divide":
    print("The quotient of your numbers is " + str(int(num1)/int(num2)))
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
else:
    print("check your spelling, capitalization, or make sure that the operation you inputed is one of the options.")
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
    messagebox.showerror(title="", message="there was an error in your responce please check for if it was an option or for spelling errors.")
# Keep the window open
