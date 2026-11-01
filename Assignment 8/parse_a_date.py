
MONTH_NAMES = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
    ]
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

def main():
    date = input("Enter a date in the format mm/dd/yyyy: ").strip()
    result = parse_date(date)
    if result:
        print(result)


def parse_date(date):
    parts = date.split('/')  # from / to break, 01/13/2345 -> ["01", "13", "2345"], it is string
    if len(parts) != 3:
        print("Error: Date must be in mm/dd/yyyy format with slashes.")
        return None
    try:
        month = int(parts[0])  # int(parts[0]) = int(01) = 1
        day = int(parts[1])  # may be user typing wrong like: ab/13/2345, so use try
        year = int(parts[2])

    except ValueError:
        print("Error: Date must be in mm/dd/yyyy format with slashes.")
        return None

    if month < MIN_MONTH or month > MAX_MONTH:
        print(f"Error: Month must be between {MIN_MONTH} and {MAX_MONTH}")
        return None

    if day < MIN_DAY or day > MAX_DAY:
        print(f"Error: Day must be between {MIN_DAY} and {MAX_DAY}.")
        return None
    
    month_name = MONTH_NAMES[month - 1]  # the word => (int(parts[0]) = int(01) = 1) - 1 = 0(index) 
    return f"{month_name} {day}, {year}"
    
if __name__=='__main__':
    main()