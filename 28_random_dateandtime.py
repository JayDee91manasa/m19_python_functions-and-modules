import random
from datetime import datetime, timedelta

# Generate a random date and time
def random_date(start, end):
    # Get a random number of seconds between the start and end dates
    random_seconds = random.randint(0, int((end - start).total_seconds()))
    return start + timedelta(seconds=random_seconds)

# Define the start and end dates
start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 12, 31)

# Generate a random date and time
random_datetime = random_date(start_date, end_date)
print("Random Date and Time:", random_datetime)