numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

double_odd_numbers = []

for i in numbers:
    if i % 2 == 0:
        double_odd_numbers.append(i*2)
        print (double_odd_numbers)

#bonus

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = 0
odd_num = 0

for i in numbers:
    if i % 2 == 0:
        even_num += i
    else:
        odd_num += i

print(even_num - odd_num)