# from employee import Employee
from monthly_employee import MonthlyEmployee
from hourly_employee import HourlyEmployee
from commission_employee import CommissionEmployee

def load_employees():
    employees = []
    # Sales 
    # full or hourly job every week 40 hour is commond, so use 40
    employees.append(HourlyEmployee("Nick DeFalco", "Hourly Employee", "Sales", 40, 1300))
    employees.append(MonthlyEmployee("Applejack Johnson", "Salaried Employee", "Sales", 44000))
    employees.append(MonthlyEmployee("Mario Dubois", "Salaried Employee", "Sales", 77200))
    
    # Engineering 
    employees.append(MonthlyEmployee("Anthony Jo", "Salaried Employee", "Engineering", 98000))
    employees.append(MonthlyEmployee("Stephanie Johnson", "Employee", "Engineering", 31200))
    
    # Maintenance 
    employees.append(CommissionEmployee("Dominic Togo", "Commission Employee", "Maintenance", 20000, 45000, 0.692))
    employees.append(HourlyEmployee("Christina Gonzalez", "Hourly Employee", "Maintenance", 40, 1029.6))
    
    # HR 
    employees.append(HourlyEmployee("Geoffrey Dav", "Hourly Employee", "HR", 40, 3380))
    return employees


def main():
    employees = load_employees()

    employee_dict = {}
    for emp in employees:
        department = emp.get_department() 
        # what this employee department
        if department not in employee_dict:  # if don't have in dict, creat new list for it
            employee_dict[department] = []
        emp_list = employee_dict[department]
        emp_list.append(emp)  # append this employee to the emp list

    for department, emp_list in employee_dict.items():
        print(f"Department: {department}")

        total_payroll = 0.00

        for emp in emp_list:
            name = emp.get_name()
            emp_id = emp.get_emp_id()
            pay = emp.calculate_pay()
            total_payroll += pay  # accumulate total salary from loop 
            if isinstance(emp, CommissionEmployee):
                base = emp.get_base_salary()
                commission_pay = emp.get_commission_pay() 
                commission_rate = emp. get_commission_rate() * 100
                print(f"    {name} ({emp_id}): ${pay:.2f}")
                print(f"\tBase ${base} + Commission ${commission_pay} ({commission_rate:1f}% of earnings)")
            else:
                print(f"    {name} ({emp_id}): ${pay:.2f}")
            
        print(f"Total Payroll: ${total_payroll:.2f}\n")

if __name__ == "__main__":
    main()




