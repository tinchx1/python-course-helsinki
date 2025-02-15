def largest():
  try:
    with open("numbers.txt") as numbers_file:
      largest_number = -float('inf')
      for line in numbers_file:
        number = int(line.strip())
        if number > largest_number:
          largest_number = number
    return largest_number
  except FileNotFoundError:
    print("The file numbers.txt was not found.")
    return None

# Ejemplo de uso
print(largest())
