text = input("Write text:")
with open("wordlist.txt") as word_list: 
  words = text.split(" ")
  checked_text = []
  for word in words:
    is_good_spelled = False
    for line in word_list:
      line_stripped = line.strip().lower()
      if word == line_stripped:
        is_not_bad_spelled = True
    if not is_good_spelled:
      checked_text.append(f"*{word}*")
    else:
      checked_text.append(word)
  print(" ".join(checked_text))

    