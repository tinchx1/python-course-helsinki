from datetime import datetime

day = int(input("day"))
month = int(input("month"))
year = int(input("year"))

new_milenium = datetime(2000, 1, 1)
new_date = datetime(year, month, day)

print(new_date - new_milenium)