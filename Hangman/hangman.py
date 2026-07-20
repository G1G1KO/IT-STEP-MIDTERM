words = {
    "fruit": ["banana", "apple", "grape", "orange", "lemon"],
    "animal": ["dinosaur", "elephant", "mouse", "tiger", "rabbit"],
    "nature": ["plant", "river", "beach", "earth", "cloud", "forest", "mountain"],
    "tech": ["python", "computer", "keyboard", "laptop", "screen", "code", "robot", "internet"],
    "science": ["planet", "universe", "atom", "space", "energy"],
    "colors": ["red", "blue", "green", "yellow", "white", "black"],  # ახალი მარტივი კატეგორია
    "places": ["garden", "market", "castle", "hospital", "aquarium"],
    "food & drinks": ["water", "bread", "coffee", "sandwich", "pizza"]
}

from random import choice

# ასოს ვალიდაცია როდესაც მომხმარებელი შეიყვანს მას
def get_input(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip().lower()
        if user_input and user_input.isalpha():
            return user_input
        else:
            print("Error: Input must contain letters only (no numbers or symbols)!")


# მთავარი პროგრამა
category = choice(list(words.keys()))

secret_word = choice(words[category])

user_lives = 10

print("=" * 10, "Hangman", "=" * 10, "\n")
print(f"HINT (Category): [{category.upper()}]\n")

display_word = ["_"] * len(secret_word)

while user_lives > 0:

    print("Guess The Word:", " ".join(display_word))

    user_input = get_input("Enter a Letter or the Whole Word: ")

    # თუ მომხმარებელმა სცადა მთლიანი სიტყვის გამოცნობა (1-ზე მეტი ასო)
    if len(user_input) > 1:
        if user_input == secret_word.lower():
            print(f"\nWOW! You guessed the full word! The Secret Word was: {secret_word.upper()}")
            break
        else:
            user_lives -= 1
            print(f"\nWrong Word Guess! Try Again ({user_lives} Lives Left)\n")
            if user_lives == 0:
                print(f"Game Over, You Lost! The Secret Word was: {secret_word.upper()}")
                break
            continue


    user_char = user_input

    # თუ მომხმარებელმა შემოიყვანა მხოლოდ 1 ასო
    char_index = secret_word.find(user_char)

    # თუ ასო არ აღმოჩნდა სიტყვაში, სიცოცხლე აკლდება და თავიდან ვეკითხებით
    if char_index == -1:
        user_lives -= 1

        print(f"\nWrong Character, Try Again ({user_lives} Lives)\n")
        
        if user_lives == 0:
            print(f"\nGame Over, You Lost! The Secret Word {secret_word.upper()}\n")
            break

        continue


    #თუ ვიპოვეთ ასო მაშინ, ის გავხადოდ uppercase, რათა იგივე ასო მარტივად მოვძებნოთ
    list_secret = list(secret_word)

    for index, char in enumerate(list_secret):
        if char.lower() == user_char:
            list_secret[index] = char.upper()
            display_word[index] = char.upper()

    secret_word = "".join(list_secret)
    

    # თუ სიტყვაში ყველა ასო upper არის მაშინ მომხმარებელს სიტყვა გამოუცვნია
    if secret_word.isupper():
        print(f"Congradulations, You Won! The Secret Word {secret_word}")
        break