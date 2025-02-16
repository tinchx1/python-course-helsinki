def filter_solutions():
  with open("solutions.csv") as solution_file, \
       open("correct.csv","w") as correct_file, \
       open("incorrect.csv","w") as incorrect_file:
    for line in solution_file:
      parts = line.strip().split(";")
      operation = parts[1]
      result = eval(operation)
      if parts[2] == str(result):
          correct_file.write(line + "\n")
      else:
          incorrect_file.write(line + "\n")
filter_solutions()