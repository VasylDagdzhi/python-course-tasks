import argparse
import os
from pathlib import Path
import glob
import os
import datetime


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

    @staticmethod
    def files():
        parser = argparse.ArgumentParser("File calculator")
        parser.add_argument("-f", help="File name.", type=str, default=Path(__file__).absolute())
        parser.add_argument("-c", help="Count words in file.", action="store_true")
        parser.add_argument("-d", help="Directory to work in.", type=str, default=Path(__file__).parent.absolute())
        parser.add_argument("-l", help="Print last file in directory listing.", action="store_true", required=False)
        args = parser.parse_args()
        dir = ""
        try:
            print(f"Counting in {args.f} file...")
            with open(args.f) as file:
                data = file.read().split(" ")
                print(f"{args.f} has {data.__len__()} words.")
            if args.c:
                if args.d:
                    dir = args.d
                else:
                    dir = Path(args.f).parent.absolute()
                print(f"Working in: {dir}")
                count = 0
                for path in os.listdir(dir):
                    # check if current path is a file
                    if os.path.isfile(os.path.join(dir, path)):
                        count += 1
                print('File count:', count)
            if args.l:
                if args.d:
                    dir = args.d
                else:
                    dir = Path(args.f).parent.absolute()
                print(f"Last file name is: '{dir}{os.listdir(dir)[-1]}'")

        except ValueError as e:
            print(e)
