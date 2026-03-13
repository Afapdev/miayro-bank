from auth import create_user
from wallet import deposit, withdraw, transfer
from storage import load_transactions

def menu():
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Transfer")
    print("6. Exit")

def show_history(username):
    history = load_transactions(username)
    if not history:
        print("No transactions yet")
        return

    print("\n=== TRANSACTION HISTORY ===")
    for action, amount, balance, target in history:
        extra = f" -> {target}" if target else ""
        print(f"{action}{extra} ₦{amount} | Balance: ₦{balance}")

def main():
    print("=== WALLET APP ===")
    print("Developed by Micael Ayanfe Robinson")

    username = input("Enter username: ")
    pin = input("Create 4-digit PIN: ")

    balance = create_user(username, pin)

    while True:
        print(f"\nWelcome, {username}")
        print(f"Wallet Balance: ₦{balance}")

        menu()
        choice = input("Choose option: ")

        if choice == "1":
            balance = deposit(username, balance)

        elif choice == "2":
            balance = withdraw(username, balance)

        elif choice == "3":
            print(f"Balance: ₦{balance}")

        elif choice == "4":
            show_history(username)

        elif choice == "5":
            balance = transfer(username, balance)

        elif choice == "6":
            print("Thank you for using Wallet App 👋")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
