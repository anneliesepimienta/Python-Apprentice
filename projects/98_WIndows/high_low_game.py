from tkinter import messagebox, simpledialog, Tk
import sys
import random


window = Tk()
window.withdraw()

# 1. Change this line to give you a random number between 1 - 100.
random_num = random.randint(1, 100)

# 2. Print out the random variable that you made in step #1
print(random_num)
# 3. Code a for loop to run steps 4-10, 10 times
for i in range(10):
    # 4. Ask the user for a guess using a pop-up window, and save their response
    guess = simpledialog.askstring(title=".", prompt="Guess a number between 1 and 100: ")
    if guess.isdigit():
        guess=int(guess)
    else:
        messagebox.showinfo(title="error", message="ERROR! THERE HAS BEEN AN ERROR FOUND IN YOUR RESPONCE. MAKE SURE THAT YOUR ANSWER ONLY INCLUDES NUMBERS. ERROR!")
        continue
    # 5. If the guess is correct
        # 6. Win. Use 'sys.exit(0)' to end the program
    if guess==random_num:
        messagebox.showinfo(title=".", message="CONGRATULATIONS!YOU HAVE WON THE GAME FOR PICKING THE CORRECT NUMBER CHOSEN!")
    # 7. if the guess is high
        # 8. Tell them it's too high
    elif guess>random_num:
        messagebox.showinfo(title=".", message="that number is waaaaaaaaaaaaaaaaaaaaaaaaaay to high of a number. try again.")
    # 9. Else if the guess is low
        # 10. Tell them it's too low
    elif guess<random_num:
        messagebox.showinfo(title=".", message="that is waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaay to low of a number. try again.")

        
#11. Outside of the loop, tell the user they lost
print("because you have used more than 10 tries to find the succesful number you have lost.")
window.mainloop()
