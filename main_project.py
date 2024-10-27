# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:45:02 2024

@author: Daniel Kiełbasiewicz, s1134543, daniel.kielbasiewicz@ru.nl
"""
import functions as mfunc
import datetime as dt
dt = dt.datetime.now()
date = dt.strftime("%d %b %Y, %A")
date_format = "%d-%m-%Y"
mfunc.ArchiveReservations(dt, date_format)
print(f"\nHello my nicest user, Welcome to booking management system!\nToday is {date}") #Only the project name was discussed with my housemate the rest is done by myself.
start_number = 1
end_number = 200
while True:
    operation = input("---\nWhat would you like to do?\n[1] - Show all reservations\n[2] - Check reservation\n[3] - Create reservation\n[4] - Exit system\n")
    match operation:
        case "1":
            print(mfunc.ShowAllReservations())
        case "2":
            data = mfunc.DataCheck()
            reservation_numbers = []
            if not data:
                print("There are no reservations in your facility")
                continue
            for line in data:
                reservation_numbers.append(line[0])
            while True:
                num = input("Type reservation number (ref) to check all details of the reservation:\n")
                if num in reservation_numbers:
                    index = reservation_numbers.index(num)
                    print(mfunc.CheckReservation(index))
                    break
                else:
                    print("There is no reservation number like yours.")
            while True:
                operation2 = input("---\nWhat would you like to do with this reservation?\n[1] - Edit reservation's status\n[2] - Delete Reservation\n[3] - Return\n")
                match operation2:
                    case "1":
                        while True:
                            status = input(f"---\nChange status of reservation:\n[1] - {mfunc.colors['bg_green']}PAID{mfunc.colors['end']}\n[2] - {mfunc.colors['bg_red']}NOT PAID{mfunc.colors['end']}\n")
                            match status:
                                case "1":
                                    data[index][13] = "PAID"
                                    mfunc.DataSave(data)
                                    print("Status has been successfully changed to 'PAID'")
                                    break
                                case "2":
                                    data[index][13] = "NOT PAID"
                                    mfunc.DataSave(data)
                                    print("Status has been successfully changed to 'NOT PAID'")
                                    break
                                case other:
                                    print("There is no option like yours. Choose different one.")
                        break
                    case "2":
                        data.pop(index)
                        mfunc.DataSave(data)
                        break
                    case "3":
                        break
                    case other:
                        print("There is no option like yours. Choose different one.")
        
        case "3":
            name = input("Type guest's Name:\n")
            while True:
                check_in = input("Type guest's check-in date (dd-mm-yyyy):\n")
                try:
                    if dt.strptime(check_in, date_format): #changing to date format
                        break
                    raise ValueError
                except ValueError:
                    print("Wrong date format, try again.")  
            while True:
                check_out = input("Type guest's check-out date (dd-mm-yyyy):\n")
                try:
                    if dt.strptime(check_out, date_format) and (dt.strptime(check_out, date_format) - dt.strptime(check_in, date_format)).days > 0:
                        break
                    raise ValueError
                except ValueError:
                    print("Wrong date format or check-out date must be later than check-in date, try again.") 
            phone = input("Type guest's phone number:\n")
            email = input("Type guest's e-mail address:\n")
            while True:
                try:
                    adults_number = int(input("Please type number of adults:\n"))
                    if adults_number < 0:
                        raise ValueError
                    elif adults_number < 1:
                        print("There has to be minimum one adult to make a reservation")
                        continue
                    break
                except ValueError:
                    print("This is not a valid number, please put positive integer number.")
            while True:
                try:
                    kids_7_15 = int(input("Please type number of kids between 7 and 15 years old:\n"))
                    if kids_7_15 < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("This is not a valid number, please put positive integer number.")
            while True:
                try:
                    kids_under_7 = int(input("Please type a number of kids under 7 years old:\n"))
                    if kids_under_7 < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("This is not a valid number, please put positive integer number.")
            while True:
                stay_type = input("Please choose guest's type of stay:\n[1] - Camper\n[2] - Tent\n[3] - Car\n")
                match stay_type:
                    case "1":
                        while True:
                            try:
                                amount = int(input("Type a number of campers:\n"))
                                if amount > 0:
                                    break
                                raise ValueError
                            except ValueError:
                                print("This is not a valid number, please put positive integer greater than 1.")
                        reservation_number = mfunc.ReservationNumberGenerator(start_number, end_number)
                        print(mfunc.CreateReservation(name, check_in, check_out, phone, email, adults_number, kids_7_15, kids_under_7, "campers", amount, date_format, reservation_number))
                        break
                    case "2":
                        while True:
                            try: 
                                amount = int(input("Type a number of tents:\n"))
                                if amount > 0:
                                    break
                                raise ValueError
                            except ValueError:
                                print("This is not a valid number, please put positive integer greater than 1.")
                        reservation_number = mfunc.ReservationNumberGenerator(start_number, end_number)
                        print(mfunc.CreateReservation(name, check_in, check_out, phone, email, adults_number, kids_7_15, kids_under_7, "tents", amount, date_format, reservation_number))
                        break
                    case "3":
                        while True:
                            try:
                                amount = int(input("Type a number of cars:\n")) 
                                if amount > 0:
                                    break
                                raise ValueError
                            except ValueError:
                                print("This is not a valid number, please put positive integer greater than 1.")
                        reservation_number = mfunc.ReservationNumberGenerator(start_number, end_number)
                        print(mfunc.CreateReservation(name, check_in, check_out, phone, email, adults_number, kids_7_15, kids_under_7, "cars", amount, date_format, reservation_number))
                        break
                    case other:
                        print("There is no option like yours. Choose different one.")
        case "4":
            print("Thanks for today. See you next time!")
            break
        case other:
            print("There is no option like yours. Choose different one.")
            

        