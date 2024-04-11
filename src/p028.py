from abc import ABC, abstractmethod


class InsufficientFundsError(Exception):
    def __init__(self, message="") -> None:
        super().__init__(message)


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Account(ABC):
    def __init__(self, branch: int, number: int, balance: float = 0) -> None:
        self.branch = branch
        self.number = number
        self.balance = balance

    @abstractmethod
    def withdraw(self, value: float) -> float:
        ...

    def deposit(self, value: float) -> float:
        self.balance += value
        return self.balance


class CurrentAccount(Account):
    def __init__(
            self,
            branch: int,
            number: int,
            balance: float = 0,
            overdraft: float = 0
    ) -> None:
        super().__init__(branch, number, balance)
        self.overdraft = overdraft

    def withdraw(self, value: float) -> float:
        if value < self.balance + self.overdraft:
            raise InsufficientFundsError()
        self.balance -= value
        return self.balance


class SavingsAccount(Account):
    def withdraw(self, value: float) -> float:
        if value < self.balance:
            raise InsufficientFundsError()
        self.balance -= value
        return self.balance


class BankCustomer(Person):
    def __init__(self, name: str, age: int, account: Account) -> None:
        super().__init__(name, age)
        self.account = account


class Bank:
    def __init__(
            self,
            accounts: list[Account] | None = None,
            branches: list[int] | None = None,
            customers: list[BankCustomer] | None = None,
    ) -> None:
        self.accounts = accounts or []
        self.branches = branches or []
        self.customers = customers or []

    def add_account(self, account: Account):
        self.accounts.append(account)

    def add_branch(self, branch: int):
        self.branches.append(branch)

    def add_customer(self, customer: BankCustomer):
        self.customers.append(customer)

    def _check_account(self, account: Account) -> bool:
        return account in self.accounts

    def _check_branch(self, branch: int) -> bool:
        return branch in self.branches

    def _check_customer(self, customer: BankCustomer) -> bool:
        return customer in self.customers

    def auth(self, customer: BankCustomer, account: Account) -> bool:
        return (
            self._check_account(account)
            and self._check_branch(account.branch)
            and self._check_customer(customer)
        )


if __name__ == "__main__":
    current_account1 = CurrentAccount(
        branch=123, number=1001, balance=500, overdraft=100)
    savings_account1 = SavingsAccount(branch=456, number=2001, balance=1000)

    john = BankCustomer(name="John", age=30, account=current_account1)
    mary = BankCustomer(name="Mary", age=25, account=savings_account1)

    bank = Bank()
    bank.add_account(current_account1)
    bank.add_account(savings_account1)
    bank.add_branch(123)
    bank.add_branch(456)
    bank.add_customer(john)
    bank.add_customer(mary)

    authenticated = bank.auth(customer=john, account=current_account1)
    print("Customer authenticated:", authenticated)

    try:
        current_account1.withdraw(700)
    except InsufficientFundsError:
        print("Error: insufficient funds")
    else:
        print("Successful withdrawal")

    savings_account1.deposit(300)
    print("Savings account balance:", savings_account1.balance)
