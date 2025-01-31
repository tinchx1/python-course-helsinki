def add_exam(sum, total, grades):
  while True:
    entry = input("Exam points and exercises completed: ")
    if entry == "":
      break
    entry = input("Exam points and exercises completed:")
    exam_points, exercises_completed = map(int, entry.split())
    exercise_points = exercises_completed // 10
    total_points = exam_points + exercise_points
    sum += total_points
    total += 1
    if exam_points >= 10:
      if total_points >= 28:
        grades[5] += 1
      elif total_points >= 24:
        grades[4] += 1
      elif total_points >= 21:
        grades[3] += 1
      elif total_points >= 18:
        grades[2] += 1
      elif total_points >= 15:
        grades[1] += 1
      else:
        grades[0] += 1
    else:
      grades[0] += 1
  return sum, total, grades

def print_statistics(sum, total, grades):
  print("Statistics:")
  if total > 0:
    print(f"Points average: {sum / total:.1f}")
    pass_percentage = (total - grades[0]) / total * 100
    print(f"Pass percentage: {pass_percentage:.1f}")
  else:
    print("Points average: 0.0")
    print("Pass percentage: 0.0")
  print("Grade distribution:")
  for grade in range(5, -1, -1):
    print(f"  {grade}: {'*' * grades[grade]}")

def main():
  sum = 0
  total = 0
  grades = [0, 0, 0, 0, 0, 0]
  sum, total, grades = add_exam(sum, total, grades)
  print_statistics(sum, total, grades)

main()