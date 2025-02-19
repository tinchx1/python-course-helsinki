def words(n: int, beginning: str):
  with open("words.txt") as words_file:
    cant = 0
    list = []
    for word in words_file:
      word = word.strip()
      if word.startswith(beginning):
        cant += 1
        list.append(word)
    if cant < n:
      raise ValueError("Not enough words")
    return list
  
word_list = words(3, "ca")
for word in word_list:
    print(word)
