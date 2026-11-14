class Employee:
    def __init__(self, name, employee_id, employee_department, employee_title):
        self.__name = name
        self.__employee_id = employee_id
        self.__employee_department = employee_department
        self.__employee_title = employee_title

    def get_name(self):
        return self.__name
    def get_employee_id(self):
        return self.__employee_id
    def get_employee_department(self):
        return self.__employee_department
    def get_employee_title(self):
        return self.__employee_title


    def set_name(self, name):
        self.__name = name
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id
    def set_employee_department(self, employee_department):
        self.__employee_department = employee_department
    def set_employee_title(self, employee_title):
        self.__employee_title = employee_title

    def __str__(self):
        return (f"Name: {self.__name}\n"
               f"ID number: {self.__employee_id}\n"
               f"Department: {self.__employee_department}\n"
               f"Title: {self.__employee_title}\n")
        
