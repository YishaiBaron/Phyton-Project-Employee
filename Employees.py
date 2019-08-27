import csv
import datetime
from tkinter import *
from tkinter import filedialog


class DB:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_from_file(self):
        data_from_reader = []
        with open (self.file_name, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data_from_reader.append(row)
            return data_from_reader

    def add_to_file(self, data):
        with open(self.file_name, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    def del_from_file(self, value_to_del):
        data = self.read_from_file()
        with open(self.file_name, "w", newline='') as f:
            writer = csv.writer(f)
            for row in data:
                if value_to_del not in row:
                    writer.writerow(row)

    def write_to_file(self, headers, data):
        with open(self.file_name, "w", newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(headers)
            for i in data:
                csv_writer.writerow(i)


class AddManually:
    def add(self):
        print ("enter employee id")
        ID = input()
        print ("enter employee name")
        name = input()
        print ("enter employee phone")
        phone = input()
        emp_data = [ID, name, phone]
        db = DB("emp_file.csv")
        db.add_to_file(emp_data)
        print("Employee added")

class AddFromFile:
    def select_file(self):
        file = filedialog.askopenfilename()
        data_from_reader = db1.read_from_file()
        db1 = DB(file)
        for i in data_from_reader:
            db2 = DB("emp_file.csv")
            db2.add_to_file(i)
    print("The data from the file added")

class DelManually:
    def del_emp(self):
        ID = input("enter id")
        db1 = DB("emp_file.csv")
        db1.del_from_file(ID)
        print("Employee removed Employee No "+ ID +" removed from the list")
        
class DeleteFromFile:
    def select_file(self):
        file = filedialog.askopenfilename()
        db1 = DB(file)
        data_from_reader = db1.read_from_file()
        for row in data_from_reader:
            ID_to_del = row[0]
            db2 = DB("emp_file.csv")
            db2.del_from_file(ID_to_del)
        print("The employees removed from the list")



class main():

    def user(self):
        print("for login press 1, for logout press 2")
        i = int(input())
        if i == 1:
           ID = input("Enter Id to Login or Logout")
           now = datetime.datetime.now()
           db = DB("AttendanceLog.csv")
           db.add_to_file([ID, now, "Login"])
           print("Login successful")
        elif i == 2:
            ID = input("Enter Id to Login or Logout")
            now = datetime.datetime.now()
            db = DB("AttendanceLog.csv")
            db.add_to_file([ID, now, "Logout"])
            print("Logout successful")



    def admin(self):
        print ("Please choose:")
        print("1. Add Manually")
        print("2. Add From File")
        print("3. Del Manually")
        print("4. Delete From File")
        print("5. Attendance Report By Emp")
        print("6. Laters Report")
        print("7. to exit")
        i=int(input())
        if i==1:
            a=AddManually()
            a.add()
        elif i==2:
            a=AddFromFile()
            a.select_file()
        elif i == 3:
            a = DelManually()
            a.del_emp()
        elif i == 4:
            a = DeleteFromFile()
            a.select_file()
        elif i == 7:
            exit()

class enterance:
    print("Hello! for User press 1. for Admin press 2")
    i = int(input())
    if i == 1:
        a=main()
        a.user()
    elif i == 2:
        a=main()
        a.admin()

