from employee import Employee
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def load_employee():  # if file exist, loda the data, if not give empty dict
    try:
        with open("employee.dat", "rb") as infile:
            employees = pickle.load(infile)
            return employees

    except FileNotFoundError:
        return {}
    
def save_employee(employees):  # save the employee to the file
    with open("employee.dat", "wb") as outfile:
        pickle.dump(employees, outfile)


def main():
    #  when the program start, first loda, put date in to the employee dict
    employees = load_employee()
    while True:
        print("Menu")
        print("-" * 30)
        print(f"{LOOK_UP}. Look up an employee")
        print(f"{ADD}. Add a new employee")
        print(f"{CHANGE}. Change an existing employee")
        print(f"{DELETE}. Delete an employee")
        print(f"{QUIT}. Quit the program")
        print()

        while True:
            try:
                choice = int(input("Enter your choice: "))
                if LOOK_UP <=  choice <= QUIT:
                    break
                else:
                    print("Enter a valid choice: ")  
                    # just tell user what problem, not input again, loop will go back to ask again

            except ValueError:
                print("Please enter a number")

        # look up
        if choice == LOOK_UP:
            emp_id = input("Enter employee ID number: ")
            if emp_id in employees:
                print(employees[emp_id])    
            else:
                print("The specified ID number was not found")

        # add
        elif choice == ADD:
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID number: ")
            emp_department = input("Enter employee department: ")
            emp_title = input("Enter employee title: ")

            # build object, store in the (employee)dict, and save it
            employees[emp_id] = Employee(name, emp_id, emp_department, emp_title)
            print("The new employee has been added.")
            save_employee(employees)  

        # change
        elif choice == CHANGE:
            emp_id = input("Enter employee ID number: ")
            if emp_id in employees:
                emp = employees[emp_id]  # get the employee
                new_name = input("Enter the new name: ")
                new_department = input("Enter the new department: ")
                new_title = input("Enter the new title: ")   

                emp.set_name(new_name)
                emp.set_employee_department(new_department)
                emp.set_employee_title(new_title)

                print("Employee information updated.")
                save_employee(employees)
            else:
                print("The specified ID number was not found")

        # delete
        elif choice == DELETE:
            emp_id = input("Enter employee ID number: ")
            if emp_id in employees:
                del employees[emp_id]  # delete this employee
                print("Employee information deleted.")
                save_employee(employees)
            else:
                print("The specified ID number was not found")

        # quit
        elif choice == QUIT:
            break


if __name__ == "__main__":
    main()
