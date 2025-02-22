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

def get_price(floor, nights):
    if floor > 0 and floor < 7:
        return nights * (80 + (20 * floor))

    elif floor < 9:
        return nights * ((50 * floor) - 100)

    elif floor == 9:
        return nights * 400
    else:
        return nights * 10,000

while True:
    check_in_check_out = simpledialog.askstring(title="", prompt="Are you here for check in or check out?")
    if check_in_check_out == "check in":
        nights= simpledialog.askinteger(title="",prompt="ok, and how many nights will you be staying with us?(you cannot stay for more than 5 nights max)")
        name = simpledialog.askstring(title = "", prompt="what will the name be that your room will be under?")
        floor= simpledialog.askinteger(title="", prompt="what floor whould you like. Each floors price gets higher because of it's better value. the 10th floor in VIP, which is worth the most.")
        
        guest_info[name]=(floor, nights)    

    elif check_in_check_out == "check out":
        checkout_name = simpledialog.askstring(title="", prompt="what name was your room under?")
        print(guest_info[checkout_name][1])
        print(guest_info[checkout_name])
        print(get_price(guest_info[checkout_name][0], guest_info[checkout_name][1]))
        del guest_info[checkout_name]

    