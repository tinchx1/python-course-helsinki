sentence = ""
last_word = ""
while True:
  word = input("Please type in a word: ")
  if word == last_word or word == "end":
    print(sentence)
    break
  sentence += word + " "
  last_word = sentence
