def everything_reversed(strings):
  i = 0
  for s in strings:
    strings[i] = strings[i][::-1]
    i += 1
  return strings[::-1]

my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)
