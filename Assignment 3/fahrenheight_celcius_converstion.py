ABSOLUTE_ZERO_OF_CELSIUS = -273.15
ABSOLUTE_ZERO_OF_FAHRENHEIT = -459.67

convert_tem = float(input("Enter the temperature you want to convert: "))
type_tem = input("Enter the type of temperature (F for Fahrenheit, C for Celsius): ")
if type_tem == "F":  # check the type
    if convert_tem >= ABSOLUTE_ZERO_OF_FAHRENHEIT: # check the number
        celsius = (convert_tem -32) * 5 / 9    
        print(f'The temperature in Celsius is: {celsius:.2f}')

    else:
        print("Invalid temperature. Please enter a temperature above absolute zero.")

elif type_tem == "C":  
    if convert_tem >= ABSOLUTE_ZERO_OF_CELSIUS: 
        fahrenheit = (convert_tem * 9 / 5) + 32    
        print(f'The temperature in Fahrenheit is: {fahrenheit:.2f}')

    else:
        print("Invalid temperature. Please enter a temperature above absolute zero.")
else:
    print("Invalid temperature type. Please enter 'F' for fahrenheit, 'C' for Celsius.")
    