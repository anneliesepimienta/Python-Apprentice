from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices

respond = simpledialog.askstring("", "choose a color from either blue, red, or white.")

if respond == "blue":
    canvas.create_oval(75, 200, 400, 450, fill=respond, outline="black")
elif respond == "red":
    canvas.create_oval(200, 200, 525, 450, fill="respond", outline="black")
elif respond == "white":
    canvas.create_rectangle(275, 100, 325, 230, fill="respond", outline="black")
else:
    messagebox.showinfo(title="", message="⚠️ An error has been found in your responce. please make sure that you are typing out what is exactly in the question as your answer ⚠️")
# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
# ()()
# (^_^)
# ( >🥕)
 

root.mainloop()
