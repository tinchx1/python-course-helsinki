string = input("Please type in a string: ")
if len(string) < 20:
  string = (20 - len(string)) * "*" + string
print(string)
