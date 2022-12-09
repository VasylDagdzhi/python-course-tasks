import argparse
from human import Human, HumanSerializer
import json
import csv


class Calculator:
    @staticmethod
    def action(a, b, action):
        if action == "+":
            print(f"{a} {action} {b} = {a + b}")
        elif action == "-":
            print(f"{a} {action} {b} = {a - b}")
        elif action == "*":
            print(f"{a} {action} {b} = {a * b}")
        elif action == "/":
            print(f"{a} {action} {b} = {a / b}")
        else:
            raise ValueError("Invalid action parameter specified.")

    @staticmethod
    def calc():
        parser = argparse.ArgumentParser("Calculator")
        parser.add_argument("a", help="First number", type=float)
        parser.add_argument("action", choices=['+', '-', '*', '/'], help="Action: [ + , - , * , / ]", type=str)
        parser.add_argument("b", help="Second number", type=float)
        args = parser.parse_args()
        try:
            Calculator.action(float(args.a), float(args.b), str(args.action))
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    Calculator.calc()
    data = Human(name="Alex", surname="Mitin", age=38)
    print(data.__dict__)

    HumanSerializer.serialize(data, "JSON")
    HumanSerializer.serialize(data, "CSV")
