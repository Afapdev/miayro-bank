from storage import save_transaction, save_balance, load_balance

def deposit(username, balance):
    amount = int(input("Enter amount to deposit: ₦"))
    if amount > 0:
        balance += amount
        save_balance(username, balance)
        save_transaction(username, "DEPOSIT", amount, balance)
        print("Deposit successful")
    else:
        print("Invalid amount")
    return balance


def withdraw(username, balance):
    amount = int(input("Enter amount to withdraw: ₦"))
    if amount > balance:
        print("Insufficient balance")
    elif amount <= 0:
        print("Invalid amount")
    else:
        balance -= amount
        save_balance(username, balance)
        save_transaction(username, "WITHDRAW", amount, balance)
        print("Withdrawal successful")
    return balance


def transfer(sender, sender_balance):
    receiver = input("Enter receiver username: ")
    amount = int(input("Enter amount to transfer: ₦"))

    receiver_balance = load_balance(receiver)

    if amount <= 0:
        print("Invalid amount")
        return sender_balance

    if amount > sender_balance:
        print("Insufficient funds")
        return sender_balance

    sender_balance -= amount
    receiver_balance += amount

    save_balance(sender, sender_balance)
    save_balance(receiver, receiver_balance)

    save_transaction(sender, "TRANSFER_OUT", amount, sender_balance, receiver)
    save_transaction(receiver, "TRANSFER_IN", amount, receiver_balance, sender)

    print(f"Transfer successful to {receiver}")
    return sender_balance
