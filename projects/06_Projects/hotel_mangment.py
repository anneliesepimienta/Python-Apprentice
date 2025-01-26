"""hi"""
"""max # of nights 5
max # of rooms 5
if not enough rooms send guest away
each night $100.00
room service $20.00
clean rooms comes with visit (tips $5.00)
check in interactive
when guest wants something or questions interactive
max poeple trying to check in 10
some popele will instead of trying to ask for a room ask questions such as directions,etc
"""
room_num = dict()



check_in = simpledialog.askstring(title="", prompt="Are you here for check in or check out?")
if check_in == "check in":
    num_nights= simpledialog.askstring(title="",prompt="ok, and how many nights will you be staying with us?(you cannot stay for more than 5 nights max)").
    name = simpledialog.askstring(title = "", prompt="what will the name be that your room will be under?")
         
#add the answers to the dictionary







if check_in == "check out":
    