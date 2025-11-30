class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def verify_pin(self, entered_pin):
        return entered_pin == self.pin

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False


# ----------------- File Handling -----------------

def load_user_data():
    try:
        with open("data.txt", "r") as file:
            pin = file.readline().strip()
            balance = float(file.readline().strip())
            return ATM(pin, balance)
    except:
        print("Error loading user data.")
        exit()


def save_user_data(atm):
    with open("data.txt", "w") as file:
        file.write(f"{atm.pin}\n{atm.balance}")


# ----------------- Main Application -----------------

def main():
    atm = load_user_data()

    print("Welcome to the ATM")

    entered_pin = input("Enter PIN: ")

    if not atm.verify_pin(entered_pin):
        print("Incorrect PIN. Exiting...")
        return

    while True:
        print("\n--- ATM Menu ---")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your Balance: ₹{atm.check_balance()}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if atm.deposit(amount):
                print("Deposit successful!")
            else:
                print("Invalid amount!")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if atm.withdraw(amount):
                print("Withdrawal successful!")
            else:
                print("Insufficient balance or invalid amount!")

        elif choice == "4":
            print("Thank you for using the ATM!")
            save_user_data(atm)
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

