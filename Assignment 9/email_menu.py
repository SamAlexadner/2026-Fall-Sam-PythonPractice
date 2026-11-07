import os
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Always read/write email.dat next to this script, regardless of the
# folder the program is run from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'email.dat')


def main():
    """Load the emails, run the menu loop, and save after each change."""
    emails = load_emails()

    while True:
        choice = get_user_choice()

        if choice == 1:
            look_up(emails)
        elif choice == 2:
            add(emails)
            save_emails(emails)
        elif choice == 3:
            change(emails)
            save_emails(emails)        
        elif choice == 4:
            delete(emails)
            save_emails(emails)
        elif choice == 5:
            save_emails(emails)
            break


def load_emails():
    """Load and return the saved emails dictionary (or an empty one)."""
    try:
        with open(FILENAME, 'rb') as infile:
            emails = pickle.load(infile)
            return emails
    except FileNotFoundError:
        return {}
    except EOFError:
        return {}



def get_user_choice():
    """Display the menu and return a validated choice."""
    print("Menu")
    print('-' * 50)
    print(f"{LOOK_UP}. Look up an email address")
    print(f"{ADD}. Add a new name and email address")
    print(f"{CHANGE}. Change an exsiting email address")
    print(f"{DELETE}. Delete a name andemail address")
    print(f"{QUIT}. Quit the program")

    try:
        choice = int(input("Enter your choice: "))
        while choice < LOOK_UP or choice > QUIT:
                choice = int(input("Enter a vaild choice: ")) 
                return choice
        return choice  
    except ValueError:
        print("Please enter a number")
    




def look_up(emails):
    """Print the email address for a name the user enters, if found."""
    name = input("Enter a name: ")
    if name in emails:
        print(f" Name: {name}")
        print(f"Email: {emails[name]}")  # open specific email, not all dict
    else:
        print("The specified name was not found.")


def add(emails):
    """Add a new name/address pair if the name isn't already present."""
    name = input("Enter name: ")
    if name not in emails:
        new_emali_address = input("Enter emial address: ")
        emails[name] = new_emali_address
        print("Name and address have benn added.")
    


def change(emails):
    """Update the address for an existing name."""
    name = input("Enter name: ")
    if name in emails:
        new_emali_address = input("Enter emial address: ")
        emails[name] = new_emali_address
        print("Information updated.")
    else:
        print("The specified name was not found.")


def delete(emails):
    """Remove a name/address pair."""
    name = input("Enter name: ")
    if name in emails:
        del emails[name]
        print("Information deleted.")


def save_emails(emails):
    """Pickle the emails dictionary to FILENAME."""
    with open(FILENAME, 'wb') as outfile:
        pickle.dump(emails,outfile)
    


if __name__ == '__main__':
    main()
