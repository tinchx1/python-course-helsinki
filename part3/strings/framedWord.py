
word = input("Word: ")
frame_width = 30
padding = (frame_width - len(word)) // 2

print("*" * frame_width)
print("*" + " " * padding + word + " " * (frame_width - len(word) - padding - 2) + "*")
print("*" * frame_width)