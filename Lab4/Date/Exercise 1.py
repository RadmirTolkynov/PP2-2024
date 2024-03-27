from datetime import datetime, timedelta

def subtract_days_from_current_date(days):
    current_date = datetime.now()

    new_date = current_date - timedelta(days=days)

    return new_date

result = subtract_days_from_current_date(5)

print(f"Current date: {datetime.now()}")
print(f"Date five days ago: {result}")
