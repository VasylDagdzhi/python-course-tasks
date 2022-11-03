# import the abstract Model class which has the basic object functionality and the colors
from framework.model import Model, Bcolors


class Salon(Model):
    file = "database/salons.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location

    @staticmethod
    def print_header():
        # printing the head and separator for the data table
        head_string = f"{'[ID]'} \t|\t {'Salon name':40} \t|\t {'Salon location':80}\t|"
        i = head_string.__len__() + 9
        separator = ""
        while i > 0:
            separator += "-"
            i -= 1
        print(Bcolors.OK + separator)
        print(head_string)
        print(separator)
        # return a defined separator string for our database table length to close the table
        return separator

    @classmethod
    def get_all_instances(cls):
        salons = Salon.get_data(cls.file)
        separator = Salon.print_header()
        # printing the main data by element
        for salon in salons:
            Salon.print_element(salon)
        # print the closing separator
        print(separator, Bcolors.RESET)

    @staticmethod
    def print_element(salon):
        print(Bcolors.OK + f"[{str(salon['key'])}] \t|\t {str(salon['name']):40} \t|\t {str(salon['location']):80}\t|")

    @staticmethod
    def get_by_id(salon_id):
        salons = Salon.get_data(Salon.file)
        # checking if the entered id is valid
        try:
            for salon in salons:
                if salon['key'] == salon_id:
                    # if we find the line with the required name we return the whole data row in an object
                    return salon
            # if the object is not returned we raise an index error
            raise IndexError  # IndexError type chosen since we are checking by an entered index (salon_id, etc.)
        except IndexError:
            print(Bcolors.WARNING + f"There is no Salon with: {salon_id} ID in the database.", Bcolors.RESET)
            prompt = input("Print the Salons database? y/n ")
            if prompt == "y" or prompt == "Y":
                Salon.get_all_instances()
                return None
            elif prompt == "n" or prompt == "N":
                return None

    @staticmethod
    def get_by_name(salon_name):
        salons = Salon.get_data(Salon.file)
        # checking if the entered id is valid
        try:
            for salon in salons:
                if salon['name'] == salon_name:
                    # if we find the line with the required name we return the whole data row in an object
                    return salon
            # if the object is not returned we raise an index error
            raise IndexError
        except IndexError:
            print(Bcolors.WARNING + f"There is no Salon with the: \'{salon_name}\' name.", Bcolors.RESET)
            prompt = input("Print the Salons database? y/n ")
            if prompt == "y" or prompt == "Y":
                Salon.get_all_instances()
                return None
            elif prompt == "n" or prompt == "N":
                return None

    @classmethod
    def edit(cls, edit_index, name, location):
        salons = cls.get_data(cls.file)
        for i in range(len(salons)):
            if salons[i]["key"] == edit_index:
                salons[i]["name"] = name
                salons[i]["location"] = location
                break  # once the required object id is saved with new values exit the loop
        cls.set_data(cls.file, salons)


class Employee(Model):
    file = "database/employees.json"

    def __new__(cls, name, email, salon_name):
        try:
            salon = Salon.get_by_name(salon_name)
            if salon is None:
                raise IndexError
            cls.name = name,
            cls.email = email,
            cls.salon_name = salon_name
            return object.__new__(cls)
        except IndexError:
            print(Bcolors.WARNING + "Please input valid Salon ID for the new employee.", Bcolors.RESET)
            return None

    def __init__(self, name, email, salon_name):
        self.name = name
        self.email = email
        self.salon_name = salon_name

    @staticmethod
    def print_header():
        # printing the head and separator for the data table
        head_string = f"{'[ID]'} \t|\t {'Name':50} \t|\t {'E-mail':50}\t|\t {'Salon name':40}\t|"
        i = head_string.__len__() + 13
        separator = ""
        while i > 0:
            separator += "-"
            i -= 1
        print(Bcolors.OK + separator)
        print(head_string)
        print(separator)
        # printing the main data
        return separator

    @classmethod
    def get_all_instances(cls):
        separator = cls.print_header()
        employees = Employee.get_data(cls.file)
        for employee in employees:
            Employee.print_element(employee)
        print(separator, Bcolors.RESET)

    @staticmethod
    def print_element(employee):
        print(f"[{str(employee['key'])}] \t|\t "
              f"{str(employee['name']):50} \t|\t "
              f"{str(employee['email']):50}\t|\t "
              f"{str(employee['salon_name']):40}\t|")

    @staticmethod
    def get_by_id(employee_id):
        employees = Employee.get_data(Employee.file)
        # checking if the entered id is valid
        try:
            for employee in employees:
                if employee['key'] == employee_id:
                    return employee
            raise IndexError
        except IndexError:
            print(Bcolors.FAIL + f"There is no employee for the input id: {employee_id}.", Bcolors.RESET)
            prompt = input("Print the employee database? y/n ")
            if prompt == "y" or prompt == "Y":
                Employee.get_all_instances()
                return None
            elif prompt == "n" or prompt == "N":
                return None

    @classmethod
    def edit(cls, edit_index, name, email, salon_name):
        employees = cls.get_data(cls.file)
        for i in range(len(employees)):
            if employees[i]["key"] == edit_index:
                employees[i]["name"] = name
                employees[i]["email"] = email
                employees[i]["salon_name"] = salon_name
                break
        cls.set_data(cls.file, employees)
