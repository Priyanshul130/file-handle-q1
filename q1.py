'''
concider a bin file emp.dat 
define 2 function insert_data() and display_data()
to store and display the records in same file 
the structure of emp.dat is EMPNo of int 
type Ename of Str Type Esal of Float type
'''

import pickle

f = open("emp.dat", "ab+")

def insert_data():
    emp_no = int(input("Enter Employee Number: "))
    ename = input("Enter Employee Name: ")
    esal = float(input("Enter Employee Salary: "))

    emp_rec = {"EMPNo": emp_no, "Ename": ename, "Esal": esal}

    pickle.dump(emp_rec, f) 
    print("Record Inserted Successfully")



def display_data():
    f.seek(0)  
    while True:
        try:
            emp_rec = pickle.load(f)
            print(f"EMPNo: {emp_rec['EMPNo']}, Ename: {emp_rec['Ename']}, Esal: {emp_rec['Esal']}")
        except EOFError:
            break

while True:
    print("1. Insert Data")
    print("2. Display Data")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        insert_data()
    elif choice == "2":
        display_data()
    elif choice == "3":
        break
    else:
        print("Choose from 1,2,3 only")
f.close() 