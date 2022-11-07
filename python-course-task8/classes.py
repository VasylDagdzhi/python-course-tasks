from decimal import Decimal
from datetime import date, datetime
from decorator import timer


class Employee:
    _name: str
    _balance: Decimal
    _rate: Decimal
    _taxes: Decimal
    _salary: Decimal
    _employment_date: date

    def __init__(
        self,
        name: str,
        balance: Decimal,
        rate: Decimal,
        taxes: Decimal,
        employment_date: date,
    ):
        self._name = (
            f"{name:<10}" + f" With the company for:   "
            f"{(datetime.now().date() - employment_date).days} days."
        )
        self._balance = balance
        self._rate = rate
        self._taxes = taxes
        self._employment_date = employment_date
        self._salary = self.calculate_salary()

    def calculate_salary(self):
        return (
            datetime.now().date()
            - self._employment_date
            # calculate how many days an employee works
        ).days * round(
            self._rate - self._rate / 100 * self._taxes, 2
        )  # calculate the daily rate with taxes

    def get_employee_data(self):
        return [self._name, self._balance, self._taxes, self._salary]


class Visualizer:
    header_string = (
        f"| {'Name':<60} | "
        f"{'Balance in $':<20} | "
        f"{'Taxes Pay in %':<20} | "
        f"{'Salary in $':<20} |"
    )
    data_string = "| {:<60} | {:<20} | {:<20} | {:<20} |"

    @classmethod
    def show_separator(cls):
        separator_length = len(cls.header_string)
        print(separator_length * "-")

    @classmethod
    def show_header(cls):
        print(cls.header_string)

    @classmethod
    def show_data(cls, data):
        print(cls.data_string.format(*data))

    @classmethod
    @timer
    def show_table(cls, employees):
        Visualizer.show_separator()
        Visualizer.show_header()
        Visualizer.show_separator()
        for employee in employees:
            Visualizer.show_data(employee.get_employee_data())
        Visualizer.show_separator()
