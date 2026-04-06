class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = 0
        self._transaction_history = []

      
        self.balance = initial_balance

    
    @property
    def account_number(self):
        return self.__account_number  

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

   
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.__balance += amount
        self._log_transaction(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient funds (Overdraft not allowed)")

        self.__balance -= amount
        self._log_transaction(f"Withdrew: {amount}")

    def get_balance(self):
        return self.__balance

    def get_transaction_history(self):
        return self._transaction_history.copy()

  
    def _log_transaction(self, message):
        self._transaction_history.append(message)



class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, initial_balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, initial_balance)
        self.__interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.__interest_rate
        self.deposit(interest)
        self._log_transaction(f"Interest applied: {interest}")



if __name__ == "__main__":
    
    acc1 = BankAccount("123456", "Kevin Ogeya", 1000)
    acc2 = SavingsAccount("654321", "Junior Ogeya", 500, 0.05)

   
    acc1.deposit(500)
    acc1.withdraw(300)

    acc2.deposit(200)
    acc2.apply_interest()

 
    print("Account 1 Balance:", acc1.get_balance())
    print("Account 2 Balance:", acc2.get_balance())

    print("\nAccount 1 Transactions:")
    for t in acc1.get_transaction_history():
        print("-", t)

    print("\nAccount 2 Transactions:")
    for t in acc2.get_transaction_history():
        print("-", t)
