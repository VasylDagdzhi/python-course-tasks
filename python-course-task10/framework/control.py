# import two main object classes which will be used in manipulations
import logging
import time

from models.models import Salon, Employee
# import a class with predefined colorful string codes for a nice output
from framework.model import Bcolors


# the main class with the data manipulation prompts and calls
class Controller:
    @staticmethod
    def add_new_salon():
        name = input("Type name of the new Salon: ")
        location = input("Type location of the new Salon: ")
        salon = Salon(name, location)
        salon.save()

    @staticmethod
    def print_all_salons():
        Salon.get_all_instances()

    @staticmethod
    def print_specific_salon():
        try:
            salon_id = int(input("Enter the id of the required Salon: "))
            salon = Salon.get_by_id(salon_id)
            if salon is not None:
                separator = Salon.print_header()
                Salon.print_element(salon)
                print(separator)
            else:
                print(Bcolors.FAIL + "\nEmployee not found.\n", Bcolors.RESET)
        except ValueError as err:
            print(Bcolors.FAIL + err.__str__(), Bcolors.RESET)
            logging.error(err)

    @staticmethod
    def remove_specific_salon():
        try:
            remove_id = int(input("Enter the id of the Salon to be removed: "))
            salon = Salon.get_by_id(remove_id)
            if salon is not None:
                Salon.delete_data(remove_id)
            else:
                print(Bcolors.FAIL + "\nWrong data inputted. Salon not removed.\n", Bcolors.RESET)
        except ValueError as err:
            print(Bcolors.FAIL + err.__str__(), Bcolors.RESET)
            logging.error(err)

    @staticmethod
    def add_new_employee():
        name = input("Type the name of the new employee: ")
        email = input("Type the email of the new employee: ")
        salon_name = input("Type the name of the Salon where the employee works: ")
        employee = Employee(name, email, salon_name)
        # since we cannot add an employee with an un-existing Salon name
        # we check if the __new__ method returned a valid object
        if employee is not None:
            employee.save()
        else:
            print(Bcolors.FAIL + "\nWrong data inputted. Employee not saved.\n", Bcolors.RESET)

    @staticmethod
    def print_all_employees():
        Employee.get_all_instances()

    @staticmethod
    def print_specific_employee():
        try:
            emp_id = int(input("Type the id of the employee: "))
            employee = Employee.get_by_id(emp_id)
            if employee is not None:
                separator = Employee.print_header()
                Employee.print_element(employee)
                print(separator)
            else:
                print(Bcolors.FAIL + "\nEmployee not found.\n", Bcolors.RESET)
        except ValueError as err:
            print(Bcolors.FAIL + err.__str__(), Bcolors.RESET)
            logging.error(err)

    @staticmethod
    def remove_specific_employee():
        try:
            remove_id = int(input("Enter the id of the employee to be removed: "))
            employee = Employee.get_by_id(remove_id)
            if employee is not None:
                Employee.delete_data(remove_id)
            else:
                print(Bcolors.FAIL + "\nWrong data inputted. Employee not removed.\n", Bcolors.RESET)
        except ValueError as err:
            print(Bcolors.FAIL + err.__str__(), Bcolors.RESET)
            logging.error(err)

    @staticmethod
    def edit_data():
        try:
            choice = int(input("1. Edit a salon.\n2. Edit an employee."))
            if choice == 1:
                Salon.get_all_instances()
                try:
                    edit_index = int(input("Input the index to be edited: "))
                    try:
                        s = Salon.get_by_id(edit_index)
                        if s is not None:
                            name = input("Input new salon name: ")
                            location = input("Input new salon location: ")
                            Salon.edit(edit_index, name, location)
                        else:
                            raise IndexError
                    except IndexError:
                        logging.error(f"\nWrong data inputted. Salon with key: [{edit_index}] not found.\n")
                except ValueError as err:
                    print(Bcolors.FAIL + err.__str__(), Bcolors.RESET)
                    logging.error(err)
                    time.sleep(3)

            elif choice == 2:
                Employee.get_all_instances()
                try:
                    edit_index = int(input("Input the index to be edited: "))
                    try:
                        e = Employee.get_by_id(edit_index)
                        if e is not None:
                            name = input("Input new employee name: ")
                            email = input("Input new employee email: ")
                            salon_name = input("Input new employee salon name: ")
                            s = Salon.get_by_name(salon_name)
                            if s is not None:
                                Employee.edit(edit_index, name, email, salon_name)
                            else:
                                logging.error(
                                    f"\nWrong data inputted. Salon: [{salon_name}] not found. "
                                    f"Employee: [{edit_index}] not edited.\n")
                                raise IndexError
                        else:
                            logging.error(f"\nWrong data inputted. Employee with key: [{edit_index}] not found.\n")
                            raise IndexError
                    except IndexError:
                        print(Bcolors.FAIL + "\nWrong data inputted. Salon data not edited.\n", Bcolors.RESET)
                        time.sleep(3)
                except ValueError as err:
                    print(Bcolors.FAIL + err.__str__(), Bcolors.RESET)
                    logging.error(err)
                    time.sleep(3)
        except ValueError as err:
            print(Bcolors.FAIL + "Wrong input.", Bcolors.RESET)
            logging.error(err)
            time.sleep(3)

    @staticmethod
    def exit_program():
        print(Bcolors.OK + "Have a good time! Bye!\n", Bcolors.RESET)
        exit(0)
