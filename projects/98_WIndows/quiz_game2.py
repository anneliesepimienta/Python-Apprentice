from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
score = 0

question= simpledialog.askstring(title="", prompt="what coding language is used for most AI?")
if question.lower == "python":
    score +=1
    messagebox.showinfo(title="", message= "CONGRATULATIONS! you are correct! your score is now " + str(score))
else:
    score -=1
    messagebox.showinfo(title = "", message = "Your answer is WRONG! the answer was python.")
messagebox.showinfo(title="", message="your final score is ." + str(score))

question2= simpledialog.askstring(title="", prompt = "what is th best coding language Python or Java?")
if question2.lower == "python":
    score +=1
    messagebox.showinfo(title="", message="CONGRATULATIONS! you are correct! your score is now ." + str(score))
else:
    score -=1
    messagebox.showinfo(title="", message="your answer is WRONG! the asnwer was python.")
messagebox.showinfo(title="", message="your final score is ." + str(score))

question3= simpledialog.askstring(title="", prompt="what is the best animal in the world?")
if question3.lower == "cat":
    score +=1
    messagebox.showinfo(title="", message="CONGRATULATIONS! your answer is correct. your score is " + str(score))
