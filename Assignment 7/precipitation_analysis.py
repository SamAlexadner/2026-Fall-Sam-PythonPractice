import os #os module to handle PATH flexibility for writing to the file

MIN_PRECIPITATION = 0.0

# Greatest monthly rainfall ever recorded: 366 inches, measured at
# Cherrapunji, Meghalaya, India, in July 1861 (Guinness World Records).
# Used as a generous upper bound since a reasonable "normal" range
# depends heavily on location.
MAX_PRECIPITATION = 366.0

# Name of the text file that stores the month names and precipitation amounts.
OUTPUT_FILE = 'precipitation.txt'


def main():
    # Create a list of the month names, January through December.
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    # Use the repetition operator to initialize the precipitation list with 0.0 for each month.
    precipitation = [0.0] * 12

    # Loop through the months and prompt the user for each month's precipitation.
    for i in range(len(months)):
        precipitation[i] = get_precipitation(months[i])

    # analyze the data using list methods and functions
    analyze_precipitation(precipitation, months)

    # Save each month name with its precipitation amount to a text file.
    path = write_precipitation_file(months, precipitation)
    print(f'Data saved to {path}')

    
def get_precipitation(months):
    while True:
        try:
            value = float(input(f"Enter precipitation for {months}: "))
            if MIN_PRECIPITATION <= value <= MAX_PRECIPITATION:
                return value
            else:
                print("Invalid input, Please enter a value between MIN_PRECIPITATION and MAX_PRECIPITATION")
        except ValueError:
            print("Invalid input, Please enter a value between MIN_PRECIPITATION and MAX_PRECIPITATION")


def analyze_precipitation(precipitation, months):
   #write your code here and then remove pass
   total_rainfall  = sum(precipitation)
   average_rainfall = total_rainfall / len(precipitation)
   highest_rainfall = max(precipitation)
   lowest_rainfall = min(precipitation)

   highest_month = months[precipitation.index(highest_rainfall)]
   lowest_month = months[precipitation.index(lowest_rainfall)]

   print(f"Total_rainfall: {total_rainfall:.2f}")
   print(f"Average_rainfall: {average_rainfall:.2f}")
   print(f"Highest_rainfall: {highest_rainfall:.2f}\t\t{highest_month}")
   print(f"Lowest_rainfall: {lowest_rainfall:.2f}\t\t{lowest_month}")


def write_precipitation_file(months, precipitation, filename=OUTPUT_FILE):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    try:
        with open(path, 'w') as output_file:
            for i in range(len(months)):
                output_file.write(f"{months[i]}, {precipitation[i]}\n")
        # add your code here
    except OSError as error:
            print(f"Could not save the data to '{path}': {error}")
            return None
    
    return path


# Call the main function only if this file is run directly.
if __name__ == '__main__':
    main()
