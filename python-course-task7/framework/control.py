from models.models import Salon, Employee
from framework.model import Bcolors


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
        salon_id = int(input("Enter the id of the required Salon: "))
        salon = Salon.get_by_id(salon_id)
        if salon is not None:
            separator = Salon.print_header()
            Salon.print_element(salon)
            print(separator)

    @staticmethod
    def remove_specific_salon():
        remove_id = int(input("Enter the id of the Salon to be removed: "))
        salon = Salon.get_by_id(remove_id)
        if salon is not None:
            Salon.delete_data(remove_id)
        else:
            print(Bcolors.FAIL + "\nWrong data inputted. Salon not removed.\n", Bcolors.RESET)

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
        emp_id = int(input("Type the id of the employee: "))
        employee = Employee.get_by_id(emp_id)
        if employee is not None:
            separator = Employee.print_header()
            Employee.print_element(employee)
            print(separator)

    @staticmethod
    def remove_specific_employee():
        remove_id = int(input("Enter the id of the employee to be removed: "))
        employee = Employee.get_by_id(remove_id)
        if employee is not None:
            Employee.delete_data(remove_id)
        else:
            print(Bcolors.FAIL + "\nWrong data inputted. Employee not removed.\n", Bcolors.RESET)

    @staticmethod
    def edit_data():
        choice = int(input("1. Edit a salon.\n2. Edit an employee."))
        if choice == 1:
            Salon.get_all_instances()
            edit_index = int(input("Input the index to be edited: "))
            s = Salon.get_by_id(edit_index)
            if s is not None:
                name = input("Input new salon name: ")
                location = input("Input new salon location: ")
                Salon.edit(edit_index, name, location)
            else:
                print(Bcolors.FAIL + "\nWrong data inputted. Salon data not edited.\n", Bcolors.RESET)
        elif choice == 2:
            Employee.get_all_instances()
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
                        raise IndexError
                else:
                    raise IndexError
            except IndexError:
                print(Bcolors.FAIL + "\nWrong data inputted. Salon data not edited.\n", Bcolors.RESET)
        else:
            print(Bcolors.FAIL + "Wrong input.", Bcolors.RESET)

    @staticmethod
    def exit_program():
        print(Bcolors.OK + "Have a good time! Bye!\n", Bcolors.RESET)
        exit(0)
