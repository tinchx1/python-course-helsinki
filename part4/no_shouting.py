def no_shouting(list):
  result = []
  for l in list:
    if not l.isupper():
      result.append(l)
  return result

my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
pruned_list = no_shouting(my_list)
print(pruned_list)