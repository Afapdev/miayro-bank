import os

DATA_DIR = "data"
BALANCE_FILE = f"{DATA_DIR}/balances.txt"
TX_FILE = f"{DATA_DIR}/transactions.txt"

os.makedirs(DATA_DIR, exist_ok=True)

def save_balance(username, balance):
    balances = load_all_balances()
    balances[username] = balance
    with open(BALANCE_FILE, "w") as f:
        for user, bal in balances.items():
            f.write(f"{user},{bal}\n")

def load_balance(username):
    balances = load_all_balances()
    return balances.get(username, 0)

def load_all_balances():
    balances = {}
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            for line in f:
                user, bal = line.strip().split(",")
                balances[user] = int(bal)
    return balances

def save_transaction(username, action, amount, balance, target=""):
    with open(TX_FILE, "a") as f:
        f.write(f"{username},{action},{amount},{balance},{target}\n")

def load_transactions(username):
    if not os.path.exists(TX_FILE):
        return []

    history = []
    with open(TX_FILE, "r") as f:
        for line in f:
            user, action, amount, balance, target = line.strip().split(",")
            if user == username:
                history.append((action, amount, balance, target))
    return history
