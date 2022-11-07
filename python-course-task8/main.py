import datetime

from classes import Visualizer, Employee
from decimal import Decimal

john = Employee(
    "John", Decimal("345.99"), Decimal("24.00"), 5, datetime.date(2022, 1, 13)
)
alex = Employee(
    "Alex", Decimal("5.00"), Decimal("33.00"), 7, datetime.date(2021, 1, 13)
)

employees = [
    Employee(
        "John", Decimal("345.99"), Decimal("24.00"), 5, datetime.date(2022, 1, 13)
    ),
    Employee("Alex", Decimal("25.00"), Decimal("23.00"), 7, datetime.date(2022, 6, 13)),
    Employee(
        "Kseniya", Decimal("0.00"), Decimal("20.00"), 10, datetime.date(2022, 8, 1)
    ),
    Employee(
        "Valeriy", Decimal("450.00"), Decimal("28.00"), 6, datetime.date(2020, 12, 29)
    ),
    Employee(
        "Vera", Decimal("5000.00"), Decimal("33.00"), 5, datetime.date(2018, 7, 23)
    ),
    Employee(
        "Suzanna", Decimal("545.00"), Decimal("29.00"), 6, datetime.date(2020, 8, 19)
    ),
    Employee(
        "Gleb", Decimal("500.00"), Decimal("28.00"), 6, datetime.date(2020, 11, 12)
    ),
]

Visualizer.show_table(employees)
