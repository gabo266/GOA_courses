def divide_numbers(num1, num2):
    if num2 != 0:  # მოვიცავთ დივიზიას 0-ზე
        result = num1 / num2
        print(f"{num1} {num2} {result}")
    else:
        print("არ შეიძლება გავყოფოთ 0-ით!")

def greet(name):
    print(f"{name}!")

from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    birth_date_obj = datetime.strptime(birth_date, "%Y-%m-%d")  # ვქმნით datetime ობიექტს დაბადების თარიღისგან
    age = today.year - birth_date_obj.year - ((today.month, today.day) < (birth_date_obj.month, birth_date_obj.day))
    print(f"თქვენი ასაკი არის: {age}")

def multiply_by_five(number):
    result = number * 5
    print(f"{number} {result}")

def print_name_and_age():
    age = int(input("შეიყვანეთ თქვენი ასაკი: "))  # ასაკი (int) იგზავნება input() ფუნქციიდან
    name = input("შეიყვანეთ თქვენი სახელი: ")  # სახელი
    print(f"თქვენი სახელი არის {name}, და თქვენ {age} წლის ხართ.")

divide_numbers(10, 2)

greet("მარიამი")

calculate_age("1995-05-15")

multiply_by_five(8)

print_name_and_age()