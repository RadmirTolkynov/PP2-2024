from datetime import datetime, timedelta

def get_dates():
    current_date = datetime.now().date()

    yesterday = current_date - timedelta(days=1)
    tomorrow = current_date + timedelta(days=1)

    return yesterday, current_date, tomorrow

yesterday, today, tomorrow = get_dates()

print(f"Yesterday: {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")
