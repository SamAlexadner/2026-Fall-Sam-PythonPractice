from pet import Pet  # don't have this one will NameError

def main():
    name = input("Enter the name of the pet: ")
    animal_types = input("Enter the type of the animal: ")
    age = int(input("Enter the age of the pet: "))
    pet = Pet(name, animal_types, age)
    print("Here is the data that you entered:")
    print(pet)

if __name__ == "__main__":
    main()
