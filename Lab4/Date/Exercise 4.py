from datetime import datetime, timedelta

def date_difference_in_seconds(date1, date2):
    time_difference = date2 - date1

    difference_in_seconds = abs(time_difference.total_seconds())

    return difference_in_seconds

# Example usage:
date1 = datetime(2022, 1, 1, 12, 0, 0)
date2 = datetime(2022, 1, 1, 13, 30, 45)

result_seconds = date_difference_in_seconds(date1, date2)

print(f"Difference between {date1} and {date2} in seconds: {result_seconds}")
