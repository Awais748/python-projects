from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += 30  

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

try:
    birth_date = datetime.strptime(dob_input, "%Y-%m-%d")

    years, months, days = calculate_age(birth_date)

    print("\n Your Age:")
    print(f"{years} years, {months} months, {days} days")

except ValueError:
    print(" Invalid date format! Please use YYYY-MM-DD")