import json
import logging
import os.path
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
        try:
            file = open(path, "r")
            data = json.loads(file.read())
        except FileNotFoundError as err:
            # if there is no file with the data or the directory where it should be, we log the error:
            logging.error(err)
            # check if the folder database exists and create if necessary:
            if not os.path.exists("database"):
                os.mkdir("database")
            try:
                # and create the file with the [] brackets as content:
                file = open(path, "w")
                file.write("[]")
            except FileNotFoundError as err:
                logging.error(err)
            finally:
                file.close()
        finally:
            file.close()
        return data

    @staticmethod
    def set_data(path, data):
        try:
            file = open(path, "w")
            file.write(json.dumps(data))
        except FileNotFoundError as err:
            # if there is no file with the data or the directory where it should be, we log the error:
            logging.error(err)
            # double-check if the folder database exists and create if necessary:
            if not os.path.exists("database"):
                os.mkdir("database")
            try:
                # and retry creating the file with the data
                file = open(path, "w")
                file.write(json.dumps(data))
            except FileNotFoundError as err:
                logging.error(err)
            finally:
                file.close()
        finally:
            file.close()

    def save(self):
        data = self.get_data(self.file)
        new_instance = self.__dict__
        if len(data) > 0:
            new_instance['key'] = data[-1]["key"] + 1
        else:
            new_instance['key'] = 1
        data.append(new_instance)
        log_string = f"Data:\t {new_instance}\tsaved to: {self.file}"
        logging.info(log_string)
        print(Bcolors.OK + log_string, Bcolors.RESET)
        self.set_data(self.file, data)

    @classmethod
    def get_all_instances(cls):
        raise NotImplementedError

    @classmethod
    def delete_data(cls, remove_id):
        instances = cls.get_data(cls.file)
        for i in range(len(instances)):
            if instances[i]["key"] == remove_id:
                log_string = f"Data:\t {instances[i]}\t removed from: {cls.file}"
                logging.info(log_string)
                print(Bcolors.OK + log_string, Bcolors.RESET)
                del instances[i]
                break
        cls.set_data(cls.file, instances)
