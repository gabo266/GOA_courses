print("hello world")

a = 5
b = 10
print(a + b)

str1 = "Hello"
str2 = "World"
print(str1 + " " + str2) 

x = 7
y = 2
result = x / y 
print(result)  

a = 5
b = 10
print(a < b) 

print(5 + 5 == 8 + 2)  

print(True and False)  
print(True or False)  
print(not True)        

print(5 > 3 and 10 < 15) 
print(10 == 10 or 5 < 3)  
print(not 7 > 5)          
print(8 != 8 and 2 == 2)  
print(9 > 7 or 4 == 4)    

for i in range(1, 11):
    print(i)

text = "Hello, World!"
for char in text:
    print(char)

i = 1
while i <= 10:
    print(i)
    i += 1

sum = 0
i = 1
while sum < 50:
    sum += i
    i += 1
print("The sum is:", sum)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers = [1, 3, 4, 5, 2]
print("Average:", calculate_average(numbers))  

def square_numbers(numbers):
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared

numbers = [3, 12, 5, 2, 6]
print("Squared list:", square_numbers(numbers)) 

my_list = [1, 2, 3]
my_list.append(4)  
print(my_list)

print(my_list)

my_string = " Hello, World! "
print(my_string.strip())  
print(my_string.upper())  
