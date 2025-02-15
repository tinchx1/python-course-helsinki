def read_fruits():
  fruits = {}
  with open("fruits.csv") as fruit_file:
    for line in fruit_file:
      tripped_line = line.strip()
      parts = tripped_line.split(";")
      fruit_name = parts[0]
      fruit_price = parts[1]
      fruits[fruit_name] = fruit_price
  return fruits
print(read_fruits())