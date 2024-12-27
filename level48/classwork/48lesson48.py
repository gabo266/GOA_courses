first_number = float(input("პირველი რიცხვი: "))
second_number = float(input("მეორე რიცხვი: "))
operator = input("ოპერატორი (+, -, *, /): ")

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "შეცდომა: 0-ზე გაყოფა არ შეიძლება"
else:
    result = "შეცდომა: არასწორი ოპერატორი"

print(f"შედეგი: {result}")
