import time

print("\nTime Zone Converter. [New York, London, Tokyo, Sydney]\n")
time.sleep(2)

source_time = input("Enter the time in the source city (HH:MM): ")

source_city = input("Enter the source city: ").capitalize()
target_city = input("Enter the target city: ").capitalize()

dst_source = input(f"Is daylight saving time observed in {source_city}? (yes/no): ").lower()

time_difference = 0

if source_city == "New York":
    if target_city == "London":
        time_difference = 5
    elif target_city == "Tokyo":
        time_difference = -14
    elif target_city == "Sydney":
        time_difference = -15
elif source_city == "London":
    if target_city == "New York":
        time_difference = -5
    elif target_city == "Tokyo":
        time_difference = -9
    elif target_city == "Sydney":
        time_difference = -10
elif source_city == "Tokyo":
    if target_city == "New York":
        time_difference = 14
    elif target_city == "London":
        time_difference = 9
    elif target_city == "Sydney":
        time_difference = 1
elif source_city == "Sydney":
    if target_city == "New York":
        time_difference = 15
    elif target_city == "London":
        time_difference = 10
    elif target_city == "Tokyo":
        time_difference = -1

if dst_source == "yes":
    time_difference += 1

source_hour, source_minute = map(int, source_time.split(":"))
target_hour = source_hour + time_difference

if target_hour < 0:
    target_hour += 24
elif target_hour >= 24:
    target_hour -= 24

print(f"\nThe time in {target_city} is {target_hour:02d}:{source_minute:02d}.")
