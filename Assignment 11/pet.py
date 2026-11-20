class Pet:
    def __init__(self, name,pet_type):
        self._name = name
        self._pet_type = pet_type

    def get_name(self):
        return self._name

    def get_pet_type(self):
        return self._pet_type
    
    def set_name(self, name):
        self._name = name

    def set_pet_type(self, pet_type):
        self._type = pet_type

    def speak(self):
        pass

class DogPet(Pet):
    def __init__(self, name):
        super().__init__(name, "Dog")

    def speak(self):
        return"Woof!"
    
class CatPet(Pet):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def speak(self):
        return"Meow!"
    
class BirdPet(Pet):
    def __init__(self, name):
        super().__init__(name, "Bird")
        
    def speak(self):
        return"Tweet!"
