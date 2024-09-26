from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    formatted_time = now.strftime("%H:%M:%S")
    current_date_and_time = f"{formatted_date} {formatted_time}"
    print(current_date_and_time)
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    result = now + timedelta(days=days_to_add)
    formatted_result = result.strftime("%Y-%m-%d")
    print(formatted_result)

display_current_datetime()

