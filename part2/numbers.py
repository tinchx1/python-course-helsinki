print("Please type in integer numbers. Type in 0 to finish.")
number_typed = 0
number_sumed = 0
while True:
  number = int(input("Number: "))
  if number == 0:
    break;
  number_typed += 1
  number_sumed += number
print(f"Numbers typed in {number_typed}")
print(f"The sum of the numbers is {number_sumed}")
print(f"The mean of the numbers is {number_sumed / number_typed}")