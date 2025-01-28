word = input("Please type in a string:")
character = input("Please type in a substring:")
index = word.find(character)
if index != -1:
  print(word[index:index+3])
  index = word.find(character, index + 1)
  if index != -1:
    print(f"The second occurrence of the substring is at index {index}")
  else:
    print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")