from employee import Employee
class HourlyEmployee(Employee):  # use PascalCase
    def __init__(self, name, emp_id, department,hours_work, hours_salary):  
        # hourworker have name and id, it also have (work how long and pay)
        super().__init__(name, emp_id,department)  
        # invoke Parent class's __init__, get the name and id
        # don't need write again: self._name = name
        self._hours_work = hours_work
        self._hours_salary = hours_salary

    def calculate_pay(self):
        return self._hours_work * self._hours_salary