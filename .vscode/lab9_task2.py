account_balance = 5000
def withdraw(amount):
    global account_balance
    if account_balance >= amount:
        account_balance = account_balance - amount
        return("Операція успішна")
    else:
        return("Недостатньо коштів")
def deposit(amount):
    global account_balance
    account_balance = amount + account_balance
print(withdraw(2000))
print(f"Баланс рахунку: {account_balance} гривень")
print(withdraw(4000))
print(f"Баланс рахунку: {account_balance} гривень")
print(deposit(1000))
print(f"Баланс рахунку: {account_balance} гривень")
