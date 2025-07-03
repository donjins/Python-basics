colors = ["red", "green", "blue"]
for color in colors:
    print(color)

word = "hello"
for letter in word:
    print(letter)

person = {"name": "John", "age": 25}
for key, value in person.items():
    print(key, value)

students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 90},
    {"name": "Charlie", "marks": 78}
]

# Loop through:
for student in students:
    print(student["name"], student["marks"])

