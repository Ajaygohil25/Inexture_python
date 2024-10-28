import csv
import os

# read data from csv files 
with open("data_fields.csv", "r") as file:
    reader = csv.reader(file) # .reader() function for read file, give data in list format
    for row in reader: 
        print(row) 

with open("data_fields.csv","r") as file:
    reader = csv.DictReader(file)  # this function give data in form of dictonary
    for d in reader:
        print(d)

# write data in csv file

with open("data_fields.csv", "w", newline='') as writeFile:
    write= csv.writer(writeFile)
    write.writerow(["Ajay","Python",4])
