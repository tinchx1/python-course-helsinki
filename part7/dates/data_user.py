from datetime import datetime, timedelta

filename = input("Filename: ")
starting_date = input("Starting date: ")
cuantity = int(input("Cuantity: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
dates = []
starting_date = datetime.strptime(starting_date, "%d.%m.%Y")

for i in range(cuantity):
    date_input = input(f"Screen time {starting_date.strftime('%d.%m.%Y')}: ")
    date = "/".join(date_input.split())
    dates.append(date)
    starting_date += timedelta(days=1)
starting_date -= timedelta(days=cuantity)
with open(filename, "w") as file:
    file.write("Time period: " + (starting_date).strftime("%d.%m.%Y") + " - " + (starting_date + timedelta(days=cuantity - 1)).strftime("%d.%m.%Y") + "\n")
    total_minutes = sum(sum(map(int, date.split("/"))) for date in dates)
    file.write("Total minutes: " + str(total_minutes) + "\n")
    file.write("Average minutes: " + str(total_minutes / cuantity) + "\n")
    for i in range(cuantity):
        file.write((starting_date + timedelta(days=i)).strftime("%d.%m.%Y") + ": " + dates[i] + "\n")