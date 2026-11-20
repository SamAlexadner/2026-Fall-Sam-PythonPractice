from employee import Employee
class MonthlyEmployee(Employee):
    def __init__(self, name, emp_id, department,month_salary):
        super().__init__(name, emp_id,department)
        self._month_salary = month_salary
    
    def calculate_pay(self): 
        return self._month_salary