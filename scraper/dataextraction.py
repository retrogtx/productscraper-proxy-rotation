"""
PLEASE READ:

This file takes in vavlues from dynamic.py
Loops through the inputted data
Adds the data in form of comma seperated values (csv) in other file
Each time dynamic.py is run, data.csv get appended
"""
import csv

data = []
print(data)


def add(name, price):
    # Append the name to the data list
    data.append(name)
    data.append(price)

    # Open the same CSV file in append mode
    f = open("data.csv", "a", newline="")
    writer = csv.writer(f)
    writer.writerow(data)

    print(data)

    f.close()
