#TODO: define Global Constants
ABSOLUTE_ZERO_OF_CELSIUS = -273.15
ABSOLUTE_ZERO_OF_FAHRENHEIT = -459.67

def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)

# TODO: complete this function which prompt user for the temperature type (C or F) until a valid input is received.
def get_temperature_type():
    type_tem = input("Enter the type of temperature (F for Fahrenheit, C for Celsius): ").upper()
    while (type_tem != "F" and type_tem != "C"):
        print("Invalid temperature type. Please enter 'F' for Fahrenheit, 'C' for Celsius.")
        type_tem = input("Enter the type of temperature (F for Fahrenheit, C for Celsius): ").upper()
    return type_tem


# TODO: complete this function which prompt user for the temperature until a valid value is received.
def get_temperature(temperature_type):
    convert_tem = float(input("Enter the temperature you want to convert: "))
    if temperature_type == "F":
        while convert_tem < ABSOLUTE_ZERO_OF_FAHRENHEIT:
            print("Invalid temperature. Please enter a temperature above absolute zero (-459.67).")
            convert_tem = float(input("Enter the temperature you want to convert: "))
    else:
        while convert_tem < ABSOLUTE_ZERO_OF_CELSIUS:
            print("Invalid temperature. Please enter a temperature above absolute zero (-273.15).")
            convert_tem = float(input("Enter the temperature you want to convert: "))
    return convert_tem

# TODO: complete this function which perform conversion based on the type
def display_conversion(temperature_type, temperature):
    if temperature_type == "F": 
        temperature = (temperature - 32) * 5 / 9
        print(f"The temperature in Celsius is: {temperature:.2f}")
    else:
        temperature = (temperature * 9 / 5) + 32        
        print(f"The temperature in Fahrenheit is: {temperature:.2f}")
    return temperature


if __name__ == "__main__":
    main()

