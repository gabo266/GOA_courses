import random

def guess_the_number():
    secret_number = random.randint(1, 100)  # Generate a secret number between 1 and 100
    guessed = False

    while not guessed:
        try:
            user_guess = int(input("Guess the number (between 1 and 100): "))
            
            if user_guess < secret_number:
                print("The secret number is higher!")
            elif user_guess > secret_number:
                print("The secret number is lower!")
            else:
                print("Congratulations! You guessed the secret number!")
                guessed = True
        except ValueError:
            print("Please enter a valid number!")

def favorite_color():
    color = input("What is your favorite color? ")
    print(f"Your favorite color is {color}!")

guess_the_number()
favorite_color()