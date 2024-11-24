numbers = [2, 4, 6, 8, 10]
product = numbers[0] * numbers[3]
print(f"{product}")

strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
middle_string = strings[len(strings)//2]
print(f"{middle_string}")

my_string = "hello"
second_char = my_string[1]
print(f"{second_char}")

products = ["კოკა-კოლა", "ნამი", "კარტოფილის ჩიფსები", "კენდი", "ლიმონათი"]

print("შეარჩიე პროდუქტი რიცხვის მიხედვით:")
print("1 - კოკა-კოლა")
print("2 - ნამი")
print("3 - კარტოფილის ჩიფსები")
print("4 - კენდი")
print("5 - ლიმონათი")

choice = int(input("შეიყვანეთ რიცხვი: "))

if 1 <= choice <= 5:
    print(f"{products[choice - 1]}")
else:
    print("არასწორი არჩევანი.")