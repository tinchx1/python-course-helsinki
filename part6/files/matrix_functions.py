#def matrix_max
def matrix_sum() -> list:
  try:
    with open("matrix.txt") as matrix:
      lines_sum = []
      for line in matrix:
        line_stripped = line.strip()
        list_elements = line_stripped.split(",")
        sum = 0
        for element in list_elements:
          sum += int(element)
        lines_sum.append(sum)
    return lines_sum
  except FileNotFoundError:
    print("The file numbers.txt was not found.")
    return None

def matrix_max() -> int:
  try:
    with open("matrix.txt") as matrix:
      greatest_number = -float("inf")
      for line in matrix:
        line_stripped = line.strip()
        list_elements = line_stripped.split(",")
        for element in list_elements:
          if int(element) > greatest_number:
            greatest_number = int(element)
      return greatest_number
  except FileNotFoundError:
    print("The file numbers.txt was not found.")
    return None

print(matrix_sum())
print(matrix_max())