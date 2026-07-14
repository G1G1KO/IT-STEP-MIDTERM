words = [
    "apple", "grape", "house", "mouse", "plant", 
    "water", "bread", "train", "clock", "smile", 
    "green", "light", "cloud", "river", "beach", 
    "earth", "music", "table", "chair", "stone",

    "python", "banana", "coffee", "orange", "flight", 
    "garden", "market", "forest", "winter", "summer", 
    "spring", "window", "doctor", "guitar", "castle", 
    "planet", "nature", "bridge", "bottle", "camera",

    "computer", "dinosaur", "elephant", "football", "mountain", 
    "keyboard", "tomorrow", "universe", "industry", "strength", 
    "language", "hospital", "treasure", "sandwich", "umbrella", 
    "calendar", "feathers", "fountain", "aquarium", "alphabet"
]

from random import choice

# ასოს ვალიდაცია როდესაც მომხმარებელი შეიყვანს მას
def get_char(prompt: str) -> str:
    while True:
       
        char = input(prompt).strip().lower()
        
        # სიგრძე უნდა იყოს ზუსტად 1 და უნდა იყოს მხოლოდ ანბანის ასო (არა ციფრი ან სიმბოლო)
        if len(char) == 1 and char.isalpha():
            return char
        else:
            print("Error: The character must be exactly one letter and cannot be a number/symbol!")



secret_word = choice(words)
user_lives = 10

print("=" * 10, "Hangman", "=" * 10, "\n")

display_word = ["_"] * len(secret_word)

while user_lives > 0:

    print("Guess The Word:", " ".join(display_word))

    user_char = get_char("Enter a Character:  ")

    # მომხმარებლის ასოს მოძებნა სიტყვაში
    char_index = secret_word.find(user_char)

    # თუ ასო არ აღმოჩნდა სიტყვაში, სიცოცხლე აკდება და თავიდან ვეკითხებით
    if char_index == -1:
        user_lives -= 1

        print(f"Wrong Character, Try Again ({user_lives} Lives)")
        
        if user_lives == 0:
            print(f"Game Over, You Lost! The Secret Word {secret_word.upper()}")
            break

        continue


    #თუ ვიპოვეთ ასო მაშინ, ის გავხადოდ uppercase, რათა იგივე ასო მარტივად მოვძებნოთ
    list_secret_word = list(secret_word)
    list_secret_word[char_index] = list_secret_word[char_index].upper()
    secret_word = "".join(list_secret_word)

    # ნაპოვნი ასო დავბეჭდოთ თავის ადგილას
    display_word[char_index] = secret_word[char_index]

    # თუ სიტყვაში ყველა ასო upper არის მაშინ მომხმარებელს სიტყვა გამოუცვნია
    if secret_word.isupper():
        print(f"Congradulations, You Won! The Secret Word {secret_word}")
        break