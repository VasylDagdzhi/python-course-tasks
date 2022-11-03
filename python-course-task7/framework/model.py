import json
from abc import ABC


class Bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


class Model(ABC):
    file = "default.json"

    @staticmethod
    def get_by_id(salon_name):
        raise NotImplementedError

    @staticmethod
    def print_header():
        raise NotImplementedError

    @staticmethod
    def print_element(instance):
        raise NotImplementedError

    @staticmethod
    def get_data(path):
        file = open(path, "r")
        data = json.loads(file.read())
        file.close()
        return data

    @staticmethod
    def set_data(path, data):
        file = open(path, "w")
        file.write(json.dumps(data))
        file.close()

    def save(self):
        data = self.get_data(self.file)
        new_instance = self.__dict__
        if len(data) > 0:
            new_instance['key'] = data[-1]["key"] + 1
        else:
            new_instance['key'] = 1
        data.append(new_instance)
        self.set_data(self.file, data)

    @classmethod
    def get_all_instances(cls):
        raise NotImplementedError

    @classmethod
    def edit(cls):
        raise NotImplementedError

    @classmethod
    def delete_data(cls, remove_id):
        instances = cls.get_data(cls.file)
        for i in range(len(instances)):
            if instances[i]["key"] == remove_id:
                del instances[i]
                break
        cls.set_data(cls.file, instances)
