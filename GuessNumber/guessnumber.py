from random import randint

#მომხმარებლის შეტანილი რიცხვის ვალიდაცია
def get_number(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Error, You Must Write an Integer only")


secret_num = randint(1, 101)
user_lives = 5

print("=" * 10, "Guess The Number", "=" * 10, "\n")

while user_lives > 0:
    user_guess = get_number("Guess The Secret Number:  ")

    if user_guess == secret_num:
        print("Congratulations, You Won")
        break

    #სიცოცხლეს ვაკლებთ მაშინვე, რადგან მომხმარებელმა ვერ გამოიცნო
    user_lives -= 1

    #ვამოწმებთ, წააგო თუ არა
    if user_lives == 0:
        print(f"You Lost! The secret number was {secret_num}")
        break

    # ვაძლევთ მინიშნებას
    hint = "Lower" if user_guess > secret_num else "Higher"
    print(f"{hint}, Try Again ({user_lives} Lives remaining)")