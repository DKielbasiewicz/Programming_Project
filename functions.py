# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:50:48 2024

@author: Daniel Kiełbasiewicz, s1134543, daniel.kielbasiewicz@ru.nl
"""
import io 
import datetime as dt
from random import randint
prices = {
    "adults" : 25,
    "kids 7-15" : 15,
    "kids under 7" : 0,
    "campers" : 35,
    "tents" : 20,
    "cars" : 30
    }

colors = {
    "bg_red" : "\033[41m",
    "bg_green" : "\033[42m",
    "end" : " \033[0m"
    }


def ReservationNumberGenerator(start_number, end_number):
    data = DataCheck()
    reservation_numbers = []
    for line in data:
        reservation_numbers.append(line[0].strip())
    while True:
        reservation_number = randint(start_number, end_number)
        if reservation_number not in reservation_numbers:
            break
    return reservation_number

def ShowAllReservations():
    data = DataCheck()
    i = 1
    print("---\n" + "This is the list of all reservations:")
    if not data:
        return "There are no reservations in your facility"
    for j in range(len(data)):
        if data[j][13] == "PAID":
            print(f"{i}. Guest's name: {data[j][1]} (ref. {data[j][0]}) stays from {data[j][2]} until {data[j][3]} ({colors['bg_green']}{data[j][13]}{colors['end']})")
        else:
            print(f"{i}. Guest's name: {data[j][1]} (ref. {data[j][0]}) stays from {data[j][2]} until {data[j][3]} ({colors['bg_red']}{data[j][13]}{colors['end']})")
        i+=1
    return ""
    
def CheckReservation(index):
    data = DataCheck() 
    values = ["Reservation number", "Person's name", "Check-in date", "Check-out date", "Length of stay in days", "Contact phone", "Contact e-mail", "Amount of adults", "Amount of kids between 7 and 15 years", "Amount of kids under 7 years", "Type of stay", "Amount", "Total cost", "Payment Status"]
    for i in range(len(data[index])):
        if i == 13:
            if data[index][i] == "PAID":
                print(values[i] + ": " + colors["bg_green"] + data[index][i] + colors["end"])
            else:
                print(values[i] + ": " + colors["bg_red"] + data[index][i] + colors["end"])
        else:
            print(f"{values[i]}: {data[index][i]}")
    return ""
    
def CreateReservation(person_name, check_in_date, check_out_date, person_phone, person_email, adults_number, kids_7_15, kids_under_7, stay_type, stay_type_amount, date_format, reservation_number):
    days = (dt.datetime.strptime(check_out_date, date_format) - dt.datetime.strptime(check_in_date, date_format)).days
    total_cost = (adults_number*prices["adults"] + kids_7_15*prices["kids 7-15"] + kids_under_7*prices["kids under 7"] + stay_type_amount*prices[stay_type])*days
    payment_status = "NOT PAID"
    new_reservation = [str(reservation_number), person_name, check_in_date, check_out_date, days, person_phone, person_email, adults_number, kids_7_15, kids_under_7, stay_type, stay_type_amount, total_cost, payment_status]
    f = io.open("reservations.txt", "a+")
    f.seek(0)
    content = f.read()
    if content:
        f.write("\n")
    f.write(str(new_reservation))
    f.close()
    return "Reservation has been created"

def DataCheck():
    data = []
    file = io.open("reservations.txt", "r")
    for line in file:
        if line == "":
            continue
        data.append(eval(line.strip()))
    file.close()
    return data

def DataSave(new_data):
    file = io.open("reservations.txt","w")
    if len(new_data) == 0:
        return file.write("")
    file.write(str(new_data[0]))
    if len(new_data) > 1:    
        for i in range(1, len(new_data)):
            file.write("\n" + str(new_data[i]))
    file.close()
    return "Data Saved"