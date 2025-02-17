def new_person(name: str, age: int):
  if name == "":
    raise ValueError("name is an empty string")
  if len(name) <  2 or len(name) > 40:
    raise ValueError("name must be 2-40 char")
  if age < 0 or age > 150:
    raise ValueError("age must be 0-150")
  return {"name": name, "age": age}
