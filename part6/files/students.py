student_info = "students1.csv"
exercise_data = "exercises1.csv"
total_notes = {}
with open(student_info) as student_file:
     for line in student_file:
         parts = line.strip().split(";")
         if parts[0] == "id" or len(parts) < 3:
             continue
         full_name = parts[1] + " " + parts[2] 
         total_notes[parts[0]] = {"name": full_name, "note": 0}
with open(exercise_data) as exercises_file:
    for line in exercises_file:
        parts = line.strip().split(";")
        if parts[0] == "id" or len(parts) < 2:
            continue
        id = parts[0]
        if id in total_notes:
          parts_without_id = parts[1:]
          total_notes[id]["note"] = sum(map(int, parts_without_id)) 
for id, info in total_notes.items():
    print(f"{info['name']}: {info['note']} exercises")