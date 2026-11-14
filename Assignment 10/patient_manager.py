from patient import Patient
from procedure import Procedure

def create_patient():
    print("Enter patient information:")
    first_name = input("First Name: ")
    middle_name = input("Middle Name: ")
    last_name = input("Lsst Name: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zip = input("ZIP: ")
    phone = input("Phone: ")
    emergency_contact = input("Emergency Contact: ")
    emergency_phone = input("Emergency Phone: ")
    
    return Patient(first_name, middle_name, last_name, address, city, state, zip, phone, emergency_contact, emergency_phone)

def create_procedure():
    print("\nEnter procedure information:")
    desc = input("Description: ")
    date = input("Date (e.g., 8-24-2019): ")
    practitioner = input("Practitioner: ")

    while True:
        try:
            if (charge := float(input("Enter the charge: "))) > 0:
                break
            print("Please enter a positive number for charge.")
        except ValueError:
            print("Please enter a valid number for charge.")
    
    return Procedure(desc, date, practitioner, charge)

def main():
    patient = create_patient()
    
    procedures = []
    print("\nAdd one or more procedures (enter 'n' to stop).")
    while True:
        procedures.append(create_procedure())
        again = input("Add another procedure? (y/n): ").strip().lower()
        if again != 'y':
            break

    print("\nPatient and Procedure Information:")
    print(patient)
    print()
    total = 0.0
    for p in procedures:
        print(p)
        print()
        total += p.get_charge()
    print(f"Total Charges: {total:.2f}")

if __name__ == "__main__":
    main()
