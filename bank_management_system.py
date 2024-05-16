class Account:
    def __init__(self, account_number, account_type, balance, account_holder_name):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.account_holder_name = account_holder_name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_account_holder_name(self):
        return self.account_holder_name


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_type, account_holder_name, initial_balance):
        new_account = Account(len(self.accounts) + 1, account_type, initial_balance, account_holder_name)
        self.accounts.append(new_account)
        return new_account

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def list_accounts(self):
        return self.accounts


# testing
bank = Bank()
account1 = bank.create_account("savings", "Nishanth", 1000)
account2 = bank.create_account("checking", "Sachii", 500)

print(account1.get_balance())  
account1.deposit(500)
print(account1.get_balance()) 

print(account2.get_balance())  
account2.withdraw(200)
print(account2.get_balance())  

print(bank.list_accounts())  