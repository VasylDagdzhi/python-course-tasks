import datetime


class Human:
    def __int__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.birth = datetime.datetime.now()


class HumanSerializer:
    pass
    # def serialize(self, obj, format):
    #     if format == "JSON":
    #         print(self.__dict__)
    #         pass
    #     elif format == "CSV":
    #         pass
    #     else:
    #         raise ValueError(f"Unrecognized format: {format}")
