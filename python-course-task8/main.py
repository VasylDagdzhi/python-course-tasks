import datetime

from classes import Employee
from datetime import date
from decimal import Decimal


john = Employee(
    name="John",
    start_time=date(2022, 10, 5),
    rate=Decimal(11),
    taxes=10,
    end_date=date.today(),
)
john.update_rate(10)
print(john.how_long())


print(date.today() - datetime.date(2022, 12, 22))
