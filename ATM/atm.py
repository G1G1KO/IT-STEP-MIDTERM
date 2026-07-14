import json

filename = "ATM/atm_users.json"



with open(filename, "r", encoding="utf-8") as file:
   users_db = json.load(file)


def save_db():
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(users_db, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Database Save Error: {e}")


def get_choice(prompt: str) -> int:
    while True:
        try:
            choice = int(input(prompt))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Wrong Input, Write (1, 2 or 3)")
        except ValueError:
            print("Error, Input Must Be a Number")


def get_number(prompt: str) -> str:
    while True:
        number = input(prompt).strip()

        if not number:
            print("Error: Number Can Not Be Empty!")
            continue

        if not number.isdigit():
            print("Error: Number must contain digits only!")
            continue

        if len(number) != 9:
            print("Error: Number's length must be exactly 9!")
            continue

        return number


def get_name(prompt: str) -> str:
    while True:
        name = input(prompt).strip()

        if not name:
            print("Error: Name Can Not Be Empty!")
            continue

        if name.isalpha():
            return name.capitalize()
        else:
            print("Error: Name must contain letters only (no numbers or symbols)!")


def get_pin(prompt: str) -> str:
    while True:
        pin = input(prompt).strip()

        if not pin:
            print("Error: Pin Can Not Be Empty")
            continue
        if not pin.isdigit():
            print("Error: Pin Must Contain Digits Only!")
            continue

        if len(pin) != 4:
            print("Error: Pin's Length Must Be Exactly 4!")
            continue

        return pin


def get_amount(prompt: str) -> float:
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                # ვამრგვალებთ მეასედებამდე (მაგალითად, 10.55 ლარი), რომ თეთრები დაცული იყოს
                return round(amount, 2)
            else:
                print("Error: Amount must be greater than 0!")
        except ValueError:
            print("Error: Please enter a valid number!")


print("=" * 10, "ATM Machine", "=" * 10)

while True:
    print("\n1. Log In Your Account")
    print("2. Create a New Account")
    print("3. Exit Program")

    user_choice_account = get_choice("Welcome, Choose (1, 2 or 3): ")

    if user_choice_account == 3:
        print("Goodbye! Thank you for using our ATM.")
        break

    # 1. ავტორიზაცია
    elif user_choice_account == 1:
        user_number = get_number("Enter Your Number: ")
        
        if user_number in users_db:
            attempts = 3  # პინის შეყვანის მცდელობების რაოდენობა
            login_success = False

            while attempts > 0:
                user_pin = get_pin(f"Enter a Pin Code (Attempts left: {attempts}): ")
                
                if user_pin == users_db[user_number]["pin"]:
                    login_success = True
                    break
                else:
                    attempts -= 1
                    if attempts > 0:
                        print("Error: Incorrect PIN Code! Try again.")
            
            if login_success:
                current_user = users_db[user_number]
                print(f"\nWelcome, {current_user['name']}!")

                while True:
                    # ბალანსის ჩვენებისას ყოველთვის ვამრგვალებთ ორ ნიშნამდე
                    print(f"\nBalance: {round(current_user['balance'], 2)} GEL")  
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Exit (Back to Main Menu)")

                    action = get_choice("Choose (1, 2 or 3): ")

                    if action == 1:
                        amount = get_amount("Enter Amount To Deposit: ")
                        current_user["balance"] = round(current_user["balance"] + amount, 2)
                        save_db()
                        print(f"Success! {amount} GEL Deposited")

                    elif action == 2:
                        amount = get_amount("Enter Amount To Withdraw: ")
                        if current_user["balance"] >= amount:
                            current_user["balance"] = round(current_user["balance"] - amount, 2)
                            save_db()
                            print(f"Success! Take Your Cash: {amount} GEL")
                        else:
                            print("Error: You Do Not Have That Much Money")
                    
                    elif action == 3:
                        print("Logging Out...")
                        break
            else:
                print("\nError: Pin limit exceeded! Returning to main menu.")
        else:
            print("Error: Phone Number Not Found In Database!")
    
    # 2. რეგისტრაცია
    elif user_choice_account == 2:
        print("\n--- Create a New Account ---")
        new_number = get_number("Enter Your Number: ")

        if new_number in users_db:
            print("Error: This number is already registered!")
            continue

        new_name = get_name("Enter Your Name: ")
        new_pin = get_pin("Create a 4-digit PIN: ")
        initial_balance = get_amount("Enter your initial deposit amount: ")

        users_db[new_number] = {
            "name": new_name,
            "pin": new_pin,
            "balance": initial_balance
        }
        
        save_db() 
        print(f"\nSuccess! Account created for {new_name}. You can now log in.")