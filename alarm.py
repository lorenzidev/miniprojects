front_door = "closed"
back_door = "open"
main_window = "open"

alarm = (front_door == "open") or (back_door == "open") or (main_window == "open")

if alarm == True:
    print('This is an automated message. I am calling police! Get out!')
else:
    print('You are good! No alarm.')



