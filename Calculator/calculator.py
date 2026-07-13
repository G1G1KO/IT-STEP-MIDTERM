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
        try:
            return float(input(prompt))
        except ValueError:
            print("Error, You Must Write a Number Only")


num1 = get_number("Enter The 1st Number:  ")
num2 = get_number("Enter The 2nd Number:  ")


while True:
    choice = input("Choose The Action (+, -, *, /):  ")
    
    if choice in ["+", "-", "*", "/"]:
        break  
    else:
        print("Error, Pick Only (+, -, *, /)")



answer = calculate(num1, num2, choice)

print(f"Answer: {answer}")

    