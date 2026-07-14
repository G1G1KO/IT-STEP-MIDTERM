import json


with open("Translator/tanslations.json", "r", encoding="utf-8") as file:
    translation_db = json.load(file)


# ენების ერთიანი საცავი
language_map = {
    1: {"name": "Georgian",
         "code": "ka"},

    2: {"name": "Russian",
         "code": "ru"},

    3: {"name": "English",
         "code": "en"}
}

# ვალიდაციის ფუნქცია (მხოლოდ 1, 2 ან 3)
def get_choice(prompt: str) -> int:
    while True:
        try:
            choice = int(input(prompt))
            if choice in language_map: # ამოწმებს არის თუ არა გასაღებებში (1, 2 ან 3)
                return choice
            else:
                print(f"Error: Must enter a number between 1 and {len(language_map)}")
        except ValueError:
            print("Error: Must enter numbers only!")


# --- მთავარი პროგრამა ---

print("=" * 10, "Translator", "=" * 10, "\n")

# ვბეჭდავთ მენიუს ლექსიკონიდან
for num, info in language_map.items():
    print(f"{num}. {info['name']}")
print("-" * 32)

# პირველი ენის არჩევა
first_choice_num = get_choice("Choose Your Language: ")
first_lang_code = language_map[first_choice_num]["code"] # იღებს კოდს, მაგ. "ka"

# მეორე ენის არჩევა (ციკლით, სანამ განსხვავებულ ენას არ აირჩევს)
while True:
    second_choice_num = get_choice("Choose Second Language: ")
    if second_choice_num == first_choice_num:
        print("Error: You cannot translate to the same language! Choose a different one.")
    else:
        break

second_lang_code = language_map[second_choice_num]["code"] 

# ვქმნით მიმართულების გასაღებს JSON-ისთვის (მაგ. "ka_en")
translation_direction = f"{first_lang_code}_{second_lang_code}"

# 4. სიტყვის შეყვანა და თარგმნა
print(f"\nTranslating from {language_map[first_choice_num]['name']} to {language_map[second_choice_num]['name']}:")
word_to_translate = input("Enter the word to translate: ").strip().lower()



translations_dct = translation_db[translation_direction]

if word_to_translate in translations_dct:
    translated_word = translations_dct[word_to_translate]
    print(f"-> Translation: {translated_word}")

else:
    print(f"-> Sorry, the word '{word_to_translate}' was not found in our database.")


    # უნდა თუ არა მომხმარებელს სიტყვის ბაზაში შენახვა
    add_choice = input("Would you like to add this word to the database? (y/n): ").strip().lower()
    
    if add_choice == 'y':
        while True:
            new_translation = input(f"Enter the translation for '{word_to_translate}' in {language_map[second_choice_num]['name']}: ").strip().lower()
            
            if not new_translation:
                print("Translation cannot be empty. Try again.")
                continue
            
            # ვამოწმებთ, რომ თარგმანი შეიცავდეს მხოლოდ ასოებს (და არა ციფრებს)
            if new_translation.isalpha():
                break
            else:
                print("Error: The translation must contain letters only (no numbers or symbols)!")
        
        # ვამატებთ ახალ სიტყვას ლოკალურ ლექსიკონში
        translation_db[translation_direction][word_to_translate] = new_translation
        
        # ვინახავთ განახლებულ ბაზას JSON ფაილში
        with open("translations.json", "w", encoding="utf-8") as file:
            json.dump(translation_db, file, indent=4, ensure_ascii=False)
            
        print(f"Successfully added! '{word_to_translate}' -> '{new_translation}' is now saved.")
    else:
        print("Okay, maybe next time!")