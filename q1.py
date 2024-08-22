import pickle

def insert_data():
    emp_no = int(input("Enter Employee Number: "))
    ename = input("Enter Employee Name: ")
    esal = float(input("Enter Employee Salary: "))

    emp_rec = {"EMPNo": emp_no, "Ename": ename, "Esal": esal}

    with open("emp.dat", "ab") as f:
        pickle.dump(emp_rec, f)
'''
def display_data():
    with open("emp.dat", "rb") as f:
        while True:
            try:
                emp_rec = pickle.load(f)
                print(f"EMPNo: {emp_rec['EMPNo']}, Ename: {emp_rec['Ename']}, Esal: {emp_rec['Esal']}")
            except EOFError:
                break'''

'''while True:
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
        print("Invalid choice. Please try again.")'''