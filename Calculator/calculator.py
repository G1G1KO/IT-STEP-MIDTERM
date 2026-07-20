#კალკულაციის ფუნქცია
def calculate(n1, n2, choice: str):
    if choice == "+":
        return n1 + n2
    
    elif choice == "-":
        return n1 - n2
    
    elif choice == "*":
        return n1 * n2
    
    elif choice == "/":
        if n2 == 0:  
            return "Error: Division by zero!"
        return n1 / n2

#ვალიდაციის ფუნქცია
def get_number(prompt: str) -> float:
    while True:
        user_input = input(prompt).strip().lower()
        
        if user_input == 'q':
            return None
            
        try:
            return float(user_input)
        except ValueError:
            print("Error: Enter a valid number or 'q' to quit!")



#მთავარი პროგრამა
print("="*10, "Calculator", "="*10,"\n")
print("(Type 'q' at any time to exit)\n")

while True:
    # პირველი რიცხვის შეყვანა
    num1 = get_number("\nEnter The 1st Number: ")
    if num1 is None:
        break 

    # მეორე რიცხვის შეყვანა
    num2 = get_number("Enter The 2nd Number: ")
    if num2 is None:
        break  # 'q' აკრიფა -> გამოდის მთავარი ციკლიდან

    # მოქმედების არჩევა
    is_quit = False
    while True:
        choice = input("Choose Action (+, -, *, /) or 'q' to quit: ").strip().lower()
        
        if choice == 'q':
            is_quit = True
            break
            
        if choice in ["+", "-", "*", "/"]:
            break  
        else:
            print("Error, Pick Only (+, -, *, /)!")

    if is_quit:
        break

    # შედეგის გამოთვლა
    answer = calculate(num1, num2, choice)
    print(f"➜ Answer: {answer}")

print("\nCalculator closed. Goodbye!")