"""hi"""
import random
from tkinter import messagebox, simpledialog, Tk
"""
check-max # of nights 5
check-max # of rooms 10
if not enough rooms send guest away
each night $100.00
room service $20.00
clean rooms comes with visit (tips $5.00)
max poeple trying to check in 10
"""


guest_info = dict()


while True:
    check_in_check_out = simpledialog.askstring(title="", prompt="Are you here for check in or check out?")
    if check_in_check_out == "check in":
        num_nights= simpledialog.askstring(title="",prompt="ok, and how many nights will you be staying with us?(you cannot stay for more than 5 nights max)")
        name = simpledialog.askstring(title = "", prompt="what will the name be that your room will be under?")
            
        guest_info[name]=(random.randint(1, 10), num_nights)    

    elif check_in_check_out == "check out":
        checkout_name = simpledialog.askstring(title="", prompt="what name was your room under?")
        print(guest_info[checkout_name][1])
        print(guest_info[checkout_name])
        del guest_info[checkout_name]