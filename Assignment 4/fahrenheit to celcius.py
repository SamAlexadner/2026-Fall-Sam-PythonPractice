celsius_degree = input("Enter a celsius degree(use integers only): ")  # let it print str first, then check
while float(celsius_degree) < 0:  # check the input correct or not
    print("Input error! Please enter a valid integer number.")
    celsius_degree = input("Enter a celsius degree(use integers only): ")  # type in again
print("Celsius \t Fahrenheit")
print("---------------------------------")
for celsius in range(0, int(celsius_degree) + 1):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} \t\t {fahrenheit:.1f}")
