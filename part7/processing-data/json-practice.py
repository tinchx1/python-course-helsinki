import json
def print_persons(filename: str):
    with open(filename, 'r') as file:
        persons = json.loads(file.read())
        for person in persons:
            hobbies = ', '.join(person['hobbies'])
            print(f"{person['name']} {person['age']} years ({hobbies})")
print_persons('persons.json')