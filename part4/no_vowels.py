def no_vowels(string):
  vowels = ["a", "e", "i", "o", "u"]
  for v in vowels:
    string = string.replace(v,"")
  return string

my_string = "this is an example"
print(no_vowels(my_string))
