from calculator import Calculator
from human import Human, HumanSerializer

if __name__ == "__main__":
    Calculator.calc()
    data = Human(name="Alex", surname="Mitin", age=38)
    print(data.__dict__)

    HumanSerializer.serialize(data, "JSON")
    HumanSerializer.serialize(data, "CSV")
