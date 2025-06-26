numbers = []
for i in range(5):
    num = int(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
    numbers.append(num)

numbers.reverse()
print("შებრუნებული სია:", numbers)
