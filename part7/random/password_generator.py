import random, string

def generate_password(length, numbers, special_characters):
    characters = []
    for i in range(length):
        if numbers:
            characters.append(random.choice(string.digits))
        if special_characters:
            characters.append(random.choice(string.punctuation))
        characters.append(random.choice(string.octdigits))

    return ''.join(characters)

for i in range(5):
    print(generate_password(10, True, True))