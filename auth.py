from storage import save_balance, load_balance

def create_user(username, pin):
    balance = load_balance(username)
    if balance == 0:
        save_balance(username, 0)
        print("User created successfully")
    else:
        print("Welcome back")
    return balance
