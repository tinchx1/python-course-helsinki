word = input("Please type in a word:")
character = input("Please type in a character:")
index = word.find(character)
while index != -1 and (index + 3) <= len(word):
  print(word[index:index+3])
  index = word.find(character, index + 1)
  