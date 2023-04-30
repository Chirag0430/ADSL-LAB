
import os


DATA_FILE = "employee_data.txt"

class Employee:
    def __init__(self, emp_id, name, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.salary = salary

def add_employee(emp):
    with open(DATA_FILE, "a") as f:
        f.write(f"{emp.emp_id},{emp.name},{emp.designation},{emp.salary}\n")
    print("Employee added successfully.")


def delete_employee(emp_id):
    lines = []
    with open(DATA_FILE, "r") as f:
        lines = f.readlines()
    with open(DATA_FILE, "w") as f:
        for line in lines:
            if not line.startswith(f"{emp_id},"):
                f.write(line)
    print("Employee deleted successfully.")



def display_employee(emp_id):
    with open(DATA_FILE, "r") as f:
        for line in f:
            if line.startswith(f"{emp_id},"):
                emp_data = line.strip().split(",")
                emp = Employee(emp_data[0], emp_data[1], emp_data[2], emp_data[3])
                print(f"Employee ID: {emp.emp_id}")
                print(f"Name: {emp.name}")
                print(f"Designation: {emp.designation}")
                print(f"Salary: {emp.salary}")
                break
        else:
            print("Employee not found.")


def main():
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, "w").close()

    while True:
        print("1. Add employee")
        print("2. Delete employee")
        print("3. Display employee information")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            designation = input("Enter employee designation: ")
            salary = input("Enter employee salary: ")
            emp = Employee(emp_id, name, designation, salary)
            add_employee(emp)
        elif choice == "2":
            emp_id = input("Enter employee ID: ")
            delete_employee(emp_id)
        elif choice == "3":
            emp_id = input("Enter employee ID: ")
            display_employee(emp_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid choice (1-4).")


if __name__ == "__main__":
    main()
