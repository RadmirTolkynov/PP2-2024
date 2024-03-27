from datetime import datetime

def drop_microseconds(input_datetime):
    new_datetime = input_datetime.replace(microsecond=0)
    return new_datetime

current_datetime = datetime.now()

result_datetime = drop_microseconds(current_datetime)

print(f"Original datetime: {current_datetime}")
print(f"Datetime without microseconds: {result_datetime}")
