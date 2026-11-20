from employee import Employee
class CommissionEmployee(Employee):
    def __init__(self, name, emp_id, department, base_salary,commision_pay,commission_rate ):
        super().__init__(name, emp_id, department)
        self._base_salary = base_salary
        self._commission_pay = commision_pay
        self._commission_rate = commission_rate

    def get_base_salary(self):
        return self._base_salary
    
    def get_commission_pay(self):
        return self._commission_pay
    
    def get_commission_rate(self):
        return self._commission_rate
    
    def calculate_pay(self):
        total = self._base_salary + (self._commission_rate * self._commission_pay)
        return total