from collections import namedtuple
from typing import NamedTuple


Transaction1 = namedtuple(
    'Transaction1',
    ['date', 'amount', 'description'],
    defaults=["UNKNOWN_DATE", 0, "UNKNOWN_DESCRIPTION"]
)


class Transaction2(NamedTuple):
    date: str = "UNKNOWN_DATE"
    amount: float = 0
    description: str = "UNKNOWN_DESCRIPTION"


transaction1 = Transaction1(
    date='2024-04-10', amount=1000.00, description='Salary')

transaction2 = Transaction2(
    date='2024-04-09', amount=-500.00, description='Rent')

transaction3 = Transaction1()
transaction4 = Transaction2()

print(transaction1.date, transaction1.amount, transaction1.description)
print(transaction2.date, transaction2.amount, transaction2.description)
print(transaction3.date, transaction3.amount, transaction3.description)
print(transaction4.date, transaction4.amount, transaction4.description)
