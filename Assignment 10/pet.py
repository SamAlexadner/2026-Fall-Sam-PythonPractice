class Pet:
    def __init__(self, name, animal_types, age):
        self.__name = name
        self.__animal_types = animal_types
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_types
   
    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_types):
        self.__animal_types = animal_types
    
    def set_age(self, age):
        self.__age = age


    def __str__(self):
        return(f"pet name: {self.__name}\n"
                f"Animal type: {self.__animal_types}\n"
                f"age of pet: {self.__age}")


