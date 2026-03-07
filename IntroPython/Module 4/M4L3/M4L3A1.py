#Get rid of the duplicates
#First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.
#Creating a dictionary with student details
# Dictionary of students (id -> details)
student_data = {
    "id1": {"name": "Sara",  "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
    "id3": {"name": "Sara",  "class": "V", "subject_integration": "english, math, science"},  # duplicate of id1
    "id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
}

result = {}
seen = set()

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])
    if unique_key not in seen:
        seen.add(unique_key)
        result[student_id] = details

# print output line by line
for k, v in result.items():
    print(k, ":", v)
