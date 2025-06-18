class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.log_file = "transactions.log"
        return cls._instance

    def log_transaction(self, account_number, transaction_type, amount, success=True):
        status = "SUCCESS" if success else "FAILED"
        log_message = f"Account: {account_number} | {transaction_type} | Amount: {amount} | Status: {status}\n"

        with open(self.log_file, "a") as file:
            file.write(log_message)


class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.accountNumber = account_number
        self.balance = initial_balance
        self.logger = Logger()

    def deposit(self, amount):
        if amount <= 0:
            self.logger.log_transaction(self.accountNumber, "DEPOSIT", amount, False)
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        self.logger.log_transaction(self.accountNumber, "DEPOSIT", amount)
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            self.logger.log_transaction(self.accountNumber, "WITHDRAW", amount, False)
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            self.logger.log_transaction(self.accountNumber, "WITHDRAW", amount, False)
            raise ValueError("Insufficient funds")

        self.balance -= amount
        self.logger.log_transaction(self.accountNumber, "WITHDRAW", amount)
        return self.balance

    def get_balance(self):
        return self.balance



if __name__ == "__main__":
    with open("transactions.log", "w") as file:
        file.write("")

    try:
        account1 = BankAccount("UA12345678", 1000)
        account2 = BankAccount("UA87654321", 500)

        print(f"Account 1 balance: {account1.get_balance()}")
        print(f"Account 2 balance: {account2.get_balance()}")

        account1.deposit(200)
        print(f"After deposit, Account 1 balance: {account1.get_balance()}")

        account1.withdraw(100)
        print(f"After withdrawal, Account 1 balance: {account1.get_balance()}")

        account2.deposit(300)
        print(f"After deposit, Account 2 balance: {account2.get_balance()}")

        account2.withdraw(1000)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTransaction log:")
    with open("transactions.log", "r") as file:
        print(file.read())