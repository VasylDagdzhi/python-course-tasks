import csv
import datetime
import json


class Human:
    name: str
    surname: str
    age: int
    birth: datetime.datetime

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.birth = datetime.datetime.now()
        self.__dict__ = {
            "name": name,
            "surname": surname,
            "age": age,
            "birth": self.birth.ctime()
        }


class HumanSerializer:
    @staticmethod
    def serialize(obj, format):
        if format == "JSON":
            print(obj.__dict__)
            with open("humans.json", 'w') as h:
                h.write(json.dumps(obj.__dict__))
        elif format == "CSV":
            with open("humans.csv", 'w') as h:
                w = csv.writer(h)
                header = []
                data = []
                for key in obj.__dict__:
                    header.append(f"'{key}'")
                    data.append(f"'{obj.__dict__[key]}'")
                w.writerow(header)
                w.writerow(data)
        else:
            raise ValueError(f"Unrecognized format: {format}")
