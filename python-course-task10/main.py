import os
import sys
import time

from models.models import Bcolors
from framework.control import Controller
import logging

try:
    date_str_time_format = "%d-%b-%y %H:%M:%S"
    message_format = "%(asctime)s - %(levelname)s - %(message)s"
    try:
        logging.basicConfig(filename="logs/main.log", format=message_format, datefmt=date_str_time_format,
                            level=logging.DEBUG)
    except FileNotFoundError as err:  # if there is no directory to store the log file we create it
        logging.error(err)
        os.mkdir("logs")
        logging.basicConfig(filename="logs/main.log", format=message_format, datefmt=date_str_time_format,
                            level=logging.DEBUG)
    finally:
        logging.info("Program session started.")

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
        flag = -1
        try:
            flag = int(input("\nMake your choice: "))
        except ValueError as err:
            # if the user inputs invalid data, like a string we log the error and prompt the input again
            logging.error(err)
            print(Bcolors.WARNING + "Invalid input.", Bcolors.RESET)
            time.sleep(3)
        if flag == 1:
            Controller.add_new_salon()
            time.sleep(3)
        elif flag == 2:
            Controller.print_all_salons()
            time.sleep(3)
        elif flag == 3:
            Controller.print_specific_salon()
            time.sleep(3)
        elif flag == 4:
            Controller.remove_specific_salon()
            time.sleep(3)
        elif flag == 5:
            Controller.add_new_employee()
            time.sleep(3)
        elif flag == 6:
            Controller.print_all_employees()
            time.sleep(3)
        elif flag == 7:
            Controller.print_specific_employee()
            time.sleep(3)
        elif flag == 8:
            Controller.remove_specific_employee()
            time.sleep(3)
        elif flag == 9:
            Controller.edit_data()
        elif flag == 0:
            Controller.exit_program()

except KeyboardInterrupt:
    print(Bcolors.WARNING, '\nInterrupted', Bcolors.RESET)
    logging.warning('Program session interrupted.')
    try:
        logging.info("Program session closed.")
        sys.exit(0)
    except SystemExit:
        exit(0)
