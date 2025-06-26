students = []

for i in range(3):
    name = input("შეიყვანეთ მოსწავლის სახელი: ")
    grades = []
    for j in range(3):
        grade = float(input(f"{name}-ის {j+1}-ე ქულა: "))
        grades.append(grade)
    average = sum(grades) / len(grades)
    students.append((name, average))

print("\nჟურნალი:")
for student in students:
    print(f"{student[0]} - საშუალო ქულა: {student[1]:.2f}")
