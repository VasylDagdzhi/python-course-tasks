from datetime import date
from decimal import Decimal
from decorator import timer


class Employee:
    def __init__(
        self,
        name: str,
        start_time: date,
        rate: Decimal,
        taxes: int,
        end_date: date = date.today(),
    ):
        self.validation(
            name=name, start_time=start_time, rate=rate, taxes=taxes, end_date=end_date
        )
        self.name = name
        self._start_time = start_time
        self._rate = rate
        self._taxes = taxes
        self._end_date = end_date
        self._balance = self._recalculate_balance()

    @staticmethod
    def validation(
        name: str, start_time: date, rate: Decimal, taxes: int, end_date: date
    ):
        if not end_date > start_time:
            raise ValueError("Start date can't be more than today.")
        if not Decimal("100") > rate > Decimal("10"):
            raise ValueError("Rate must be in between 10 and 100.")
        if not 99 >= taxes > 1:
            raise ValueError("Taxes must be in between 1 and 99.")
        if not 20 >= len(name) >= 4:
            raise ValueError("Name must have from 4 to 20 chars.")

    def days(self):
        return (self._end_date - self._start_time).days

    def how_long(self):
        return f"{self.name} has worked for {self.days()} days."

    def _recalculate_balance(self):
        self._balance = self._rate * self.days()
        return self._balance

    @timer
    def update_rate(self, rate):
        self._rate = Decimal(rate)
        self._balance = self._recalculate_balance()
        return self._rate

    @property
    def rate(self):
        return self._rate
