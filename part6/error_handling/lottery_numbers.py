def filter_incorrect():
  with open("lottery_numbers.csv") as lottery_file, \
       open("correct.csv","w") as correct_file:
    for line in lottery_file:
      parts = line.strip().split(";")
      week = parts[0]
      number_week = week.split(" ")[1]
      if not number_week.isdigit():
        continue

      numbers = parts[1].split(",")
      if len(numbers) != 7:
        continue

      if not all(map(lambda x: x.isdigit(), numbers)):
        continue

      if not all(map(lambda x: 1 <= int(x) <= 40, numbers)):
        continue

      if not all(map(lambda x: numbers.count(x) == 1, numbers)):
        continue

      correct_file.write(line + "\n")

filter_incorrect()