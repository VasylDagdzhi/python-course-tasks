from models.models import Bcolors
from framework.control import Controller

while True:
    print(Bcolors.RESET +
          "1. Add new Salon.\n"
          "2. Print all Salons.\n"
          "3. Print Salon by id.\n"
          "4. Remove Salon by id.\n"
          "5. Add new employee.\n"
          "6. Print all employees.\n"
          "7. Print employee by id.\n"
          "8. Remove employee by id.\n"
          "9. Edit existing data.\n"
          "0. Exit")
    flag = int(input("\nMake your choice: "))
    if flag == 1:
        Controller.add_new_salon()
    elif flag == 2:
        Controller.print_all_salons()
    elif flag == 3:
        Controller.print_specific_salon()
    elif flag == 4:
        Controller.remove_specific_salon()
    elif flag == 5:
        Controller.add_new_employee()
    elif flag == 6:
        Controller.print_all_employees()
    elif flag == 7:
        Controller.print_specific_employee()
    elif flag == 8:
        Controller.remove_specific_employee()
    elif flag == 9:
        Controller.edit_data()
    elif flag == 0:
        Controller.exit_program()
