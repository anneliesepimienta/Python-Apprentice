"""hi"""
import messagebox, simpledialog, Tk
import random

"""
check-max # of nights 5
check-max # of rooms 10
if not enough rooms send guest away
each night $100.00
room service $20.00
clean rooms comes with visit (tips $5.00)
max poeple trying to check in 10
"""


check_in = simpledialog.askstring(title="", prompt="Are you here for check in or check out?")
if check_in == "check in":
    num_nights= simpledialog.askstring(title="",prompt="ok, and how many nights will you be staying with us?(you cannot stay for more than 5 nights max)")
    name = simpledialog.askstring(title = "", prompt="what will the name be that your room will be under?")
         
#add the answers to the dictionary

guest_info = dict()
guest_info[name]=(random.randint(1, 10), num_nights)
    