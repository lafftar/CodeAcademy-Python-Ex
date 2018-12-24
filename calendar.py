# This programis a Calender, it allows users to add events, update existing events and delete events.
from time import sleep, strftime

first_name = "TJ"
calender = {"dates": "events"}


def welcome():
    print('Hello' + first_name)
    print('Just a sec, the calender is loading.')
    sleep(1)
    print(strftime("%A %B %d, %Y"))
    print(strftime("%H:%M:%S"))
    print("What would you like to do?")


def start_calender():
    welcome()
    start = True
    while start:
        user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit:")
        user_choice = user_choice.upper()
        if user_choice == "V":
            if len(calender.keys()) == 0:
                print("The calender is empty.")
            else:
                print(calender)
        elif user_choice == "U":
            date = input("What date? ")
            update = input("Enter the update: ")
            calender[date] = update
            print("Update successful")
            print(calender)
        elif user_choice == "A":
            event = input("Enter event: ")
            date = int(input("Enter date (MM/DD/YYYY): "))
            if len(date) > 10 or date < int(strftime("%Y")):
                print("Invalid date has been entered.")
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                calender[date] = event
                print("Event successfully added.")
                print(calender)
        elif user_choice == "D":
            if len(calender.keys) < 1:
                print("Calender is empty.")
            else:
                event = input("What event?")
                for stuff in calender.keys():
                    if event == calender[date]:
                        del calender[date]
                        print("Event successfully deleted.")
                        print(calender)
                    else:
                        print("Incorrect event specified.")
        elif user_choice == "X":
            start = False
        else:
            print("Invalid command entered.")
            start = False


start_calender()
