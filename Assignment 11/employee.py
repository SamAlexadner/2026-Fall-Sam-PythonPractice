class Employee:
    def __init__(self, name, emp_id, department):
        self._name = name
        self._emp_id = emp_id
        self._department = department

    def get_name(self):
        return self._name
    def get_emp_id(self):
        return self._emp_id
    def get_department(self):
        return self._department

    def set_name(self, name):
        self._name = name
    def set_emp_id(self, emp_id):
        self._emp_id = emp_id
    def set_department(self, department):
        self._department = department

    def calculate_pay(self):
        pass


# class HourlyEmployee(Employee):  # use PascalCase
#     def __init__(self, name, emp_id, department,hours_work, hours_salary):  
#         # hourworker have name and id, it also have (work how long and pay)
#         super().__init__(name, emp_id,department)  
#         # invoke Parent class's __init__, get the name and id
#         # don't need write again: self._name = name
#         self._hours_work = hours_work
#         self._hours_salary = hours_salary

#     def calculate_pay(self):
#         return self._hours_work * self._hours_salary

# class MonthlyEmployee(Employee):
#     def __init__(self, name, emp_id, department,month_salary):
#         super().__init__(name, emp_id,department)
#         self._month_salary = month_salary
    
#     def calculate_pay(self): 
#         return self._month_salary

# class CommissionEmployee(Employee):
#     def __init__(self, name, emp_id, department, base_salary,commission_rate, sales):
#         super().__init__(name, emp_id, department)
#         self._base_salary = base_salary
#         self._commission_rate = commission_rate
#         self._sales = sales

#     def get_commission_pay(self):
#         commission = self._commission_rate * self._sales
#         return f"Base Salary: {self._base_salary}, Commission: {commission}"
    
#     def calculate_pay(self):
#         base = self._base_salary
#         commission = self._commission_rate * self._sales
#         return (base, commission)
    

     
