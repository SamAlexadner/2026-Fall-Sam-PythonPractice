class Procedure:
    def __init__(self, procedure_infromation, date, practitioner, charge):
        self.__procedure_infromation = procedure_infromation
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge

    def get_procedure_infromation(self):
        return self.__procedure_infromation
    def get_date(self):
        return self.__date
    def get_practitioner(self):
        return self.__practitioner
    def get_charge(self):
        return self.__charge

    def set_procedure_infromation(self, procedure_infromation):
        self.__procedure_infromation = procedure_infromation
    def set_date(self, date):
        self.__date = date
    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner
    def set_charge(self, charge):
        self.__charge = charge

    def __str__(self):
        return(f"Procedure: {self.__procedure_infromation}\n"
               f"Date: {self.__date}\n"
               f"Practitioners: {self.__practitioner}\n"
               f"Charge: {self.__charge:.2f}\n")

