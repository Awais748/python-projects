balance = 0

def show_balance():
    global balance
    print(f"Your current balance is: ${balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"${amount} deposited successfully!")
    else:
        print("Invalid amount! Deposit must be greater than 0.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount! Withdrawal must be greater than 0.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"${amount} withdrawn successfully!")


is_running = True

while is_running:
    print("\nWelcome to the Bank")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using our bank. Goodbye!")
        is_running = False
    else:
        print("Invalid choice! Try again.")