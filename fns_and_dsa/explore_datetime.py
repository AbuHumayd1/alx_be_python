import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current Date and Time:")
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date(number_of_days):
    future_date = datetime.datetime.now() + timedelta(days=number_of_days)
    print("Future date: ", future_date.strftime("%Y-%m-%d %H:%M:%S"))
calculate_future_date(number_of_days)
    