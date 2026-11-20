# from pet import Pet
from pet import DogPet
from pet import CatPet
from pet import BirdPet

def print_menu():
    print("\nPet Menu")
    print("1. Add Dog")
    print("2. Add Cat")
    print("3. Add Bird")
    print("4. Show All Pets")
    print("5. Exit")


def main():
    pets = []

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        try:
            choice = int(choice)
            if 1 <= choice <= 5:
                if choice == 1:
                    name = input("Enter your dog's name: ")
                    pets.append(DogPet(name))  # creat dog name, put in list
                elif choice == 2:
                    name = input("Enter your cat's name: ")
                    pets.append(CatPet(name))
                elif choice == 3:
                    name = input("Enter your bird's name: ")
                    pets.append(BirdPet(name))
                elif choice == 4:
                    print("Your Pets:")
                    for pet in pets:
                        print(f"{pet.get_name()} the {pet.get_pet_type()} says {pet.speak()}")
                elif choice == 5:
                    print("Goodbye!")
                    break
            else:
                print("Enter a valid choice: ")
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    main()