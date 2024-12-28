from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
prompt = "If a cat walks up to you and meows in an angry way you have to make sure that you are doing these exact steps."
noun = simpledialog.askstring(title = "", prompt = " enter a noun to start your story")
liquid = simpledialog.askstring(title="", prompt="enter a liquid to continue")
body_part = simpledialog.askstring(title="", prompt="enter a body part")
verb = simpledialog.askstring(title="", prompt="enter a verb to continue")
place = simpledialog.askstring(title="", prompt="enter a place to finish your story")


story = (
   f"cats are very territorial and like to claim their {noun}. so you must be very careful with these steps."
   f"they will fight if needed so you might want to offer something such as {liquid} to calm them down and warm up to you."
   f"and if that doesn't please them they will likely bite your {body_part} off."
   f" as soon as this happens they will emediatly start {verb} going crazy in the process."
   f"when this happens you might want to emediatly escape to the nearest {place}, and hope to survive."
)
messagebox.showinfo(message=story)
window.mainloop()