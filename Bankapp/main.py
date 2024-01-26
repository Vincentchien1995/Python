class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Customer[{self.id}, {self.firstname}, {self.lastname}]'

class Account:
    last_id = 1000

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0
        self.transactions=[]

    def deposit(self, amount):
        #TODO implement
        if type(amount) != int or amount < 0:
            raise InvalidAmountException(f'Amount is invalid {amount}')
        self._balance += amount
        transaction = AccountTransaction(self, 'Deposit', amount)
        self.transactions.append(transaction)

    def charge(self, amount):
        #TODO implement
        if type(amount) != int or amount < 0:
            raise InvalidAmountException(f'Amount is invalid {amount}')
        if amount > self._balance:
            raise InsufficientFundsException(f'Insufficient balance: {self._balance}')
        self._balance -= amount
        transaction = AccountTransaction(self, 'Charge', amount)
        self.transactions.append(transaction)

    def __repr__(self):
        return f'Account[{self.id}, {self.customer.lastname}, {self._balance}]'
    def get_transaction_history(self):
        return self.transactions

class Bank:
    def __init__(self):
        self.customer_list = []
        self.account_list = []
    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c
    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a
    def transfer(self, from_account_id, to_account_id, amount):
        #TODO
        if type(amount) != int or amount <= 0:
            raise InvalidAmountException(f'Invalid amount: {amount}')
        from_account = self.find_account(from_account_id)
        to_account = self.find_account(to_account_id)
        if from_account._balance < amount:
            raise InsufficientFundsException(f'Insufficient funds in account {from_account_id}')
        from_account.charge(amount)
        to_account.deposit(amount)
    def find_account(self, account_id):
        #TODO
        for account in self.account_list:
            if account.id == account_id:
                return account
        return None

    def __repr__(self):
        return f'Bank[{self.customer_list}; {self.account_list}]'
class AccountTransaction:
    def __init__(self, account, transaction_type, amount):
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount

    def __repr__(self):
        return f'AccountTransaction[{self.account.id}, {self.transaction_type}, {self.amount}]'
class BankException(Exception):
    pass
class InsufficientFundsException(BankException):
    pass
class InvalidAmountException(BankException):
    pass



# Create a bank instance
bank = Bank()

# Create customers
customer1 = bank.create_customer("Adam", "Doe")
customer2 = bank.create_customer("Ella", "Walter")
customer3 = bank.create_customer('Sheldon','Smith')

# Create accounts for customers
account1 = bank.create_account(customer1)
account2 = bank.create_account(customer2)
account3 = bank.create_account(customer3)

# Deposit and charge on accounts
account1.deposit(1200)
account2.deposit(600)
account3.deposit(1000)
account1.charge(300)
account2.charge(200)

# Transfer funds from account1 to account2
try:
    bank.transfer(account1.id, account2.id, 300)
    print("Funds transferred successfully.")
except InvalidAmountException as e:
    print(f"Invalid amount: {e}")
except InsufficientFundsException as e:
    print(f"Insufficient funds: {e}")

# Get transaction history for account1
print(f"Transaction history for Account {account1.id}:")
transactions_account1 = account1.get_transaction_history()
for transaction in transactions_account1:
    print(transaction)

# Get transaction history for account2
print(f"Transaction history for Account {account2.id}:")
transactions_account2 = account2.get_transaction_history()
for transaction in transactions_account2:
    print(transaction)

# Display customer and account information
print("Customers:")
for customer in bank.customer_list:
    print(customer)

print("Accounts:")
for account in bank.account_list:
    print(account)
