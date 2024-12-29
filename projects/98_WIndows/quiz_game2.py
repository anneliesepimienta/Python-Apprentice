from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
score = 0

question= simpledialog.askstring(title="", prompt="what coding language is used for most AI?")
if question == "python":
    score +=1
    messagebox.showinfo(title="", message= "CONGRATULATIONS! you are correct! your score is now " + str(score))
else:
    score -=1
    messagebox.showinfo(title = "", message = "Your answer is WRONG! the answer was python.")
messagebox.showinfo(title="", message="your final score is ." + str(score))

question2= simpledialog.askstring(title="", prompt = "what is the best coding language Python or Java?")
if question2 == "python":
    score +=1
    messagebox.showinfo(title="", message="CONGRATULATIONS! you are correct! your score is now ." + str(score))
else:
    score -=1
    messagebox.showinfo(title="", message="your answer is WRONG! the asnwer was python.")
messagebox.showinfo(title="", message="your final score is ." + str(score))

question3= simpledialog.askstring(title="", prompt="what is the best animal in the world?")
if question3 == "cat":
    score +=1
    messagebox.showinfo(title="", message="CONGRATULATIONS! your answer is correct. your score is " + str(score))
else:
    score -=1
    messagebox.showinfo(title="", message="Your answer is WRONG! the answer was cat.")
messagebox.showinfo(title="", message="yout final score is " + str(score))

score = 0  

questions = [  
    "what is the best coding language Python or Java?",  
    "what coding language is used for most AI?",
    "what is the best animal in the world?" 
]  

answers = ["python", "python", "cat"]

for i in range(len(questions)):  
    response = simpledialog.askstring(None, questions[i])  

    if response.lower() == answers[i]:  
        score += 1  
        print("Correct! Your score is " + str(score))  
    else:  # ;
        score -= 1  
        messagebox.showerror(message="WRONG! It's " + answers[i] + " of course!")  

messagebox.showinfo(message="Your final score is " + str(score))  
window.mainloop()