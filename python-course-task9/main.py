# TASK 1
# Створити логер який дозволяє працювати з файлами як звичайний open,
# але разом з тим в файл logs.txt записує:
# коли був відкритий файл, назва файла, коли закритий файл
# для інформації про час можемо використати datetime.now()
# приклад відпрацювання
# with my_custom_manager('file.txt', 'r') as f:
#     f.read()
# В файл буде записано
# 2022-07-11 22:17:59.782551 file.txt OPEN
# 2022-07-11 22:18:00.782551 file.txt CLOSE
import json
from datetime import datetime
import csv


class Logger:
    def __init__(self, filename, mode="a+"):
        self.file = open(filename, mode)

    def __enter__(self):
        self.file.write(str(datetime.now()) + " " + self.file.name + " " + "OPEN\n")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write(str(datetime.now()) + " " + self.file.name + " " + "CLOSE\n")
        self.file.close()

    @staticmethod
    def file_to_csv(source_file, destination_file):
        with open(source_file, 'r') as infile, open(destination_file, 'w') as outfile:
            stripped = (line.strip() for line in infile)
            lines = (line.split("\n") for line in stripped if line)
            writer = csv.writer(outfile)
            for line in lines:
                split_lines = (l.split(" ") for l in line if l)
                for s in split_lines:
                    line_to_write = [(s[0] + " " + s[1]), s[2], s[3]]
                    writer.writerow(line_to_write)

    # TASK 3 (з зірочкою)
    # Написати ф-цію, яка обраховує з файла logs.csv скільки раз був відкритий файл і його остання дата відкриття.
    # Цю інформацію записати в logs.json. Приклад:
    # {
    #     "file.txt": {
    #         "count": 2,
    #         "last_time_opened": "2022-07-11 22:17:59.782551"
    #     }
    # }
    @staticmethod
    def log_file_details(csv_source, json_destination):
        with open(csv_source, 'r') as infile, open(json_destination, 'w') as outfile:
            stripped = (line.strip() for line in infile)
            # read all the lines in the csv file:
            lines = (line.split("\n") for line in stripped if line)
            # unbox the date and timestamp details from the last line read:
            last_time_data = (str([*lines][-1][0]).split(","))
            last_date = last_time_data[0].split(" ")
            # save the initial file name received:
            initial_file_name = last_time_data[1]
            # reset the csv file cursor:
            infile.seek(0)
            # start counting how many times the initial file was open:
            opened_times = 0
            # get the data again after unboxing and file cursor reset:
            stripped = (line.strip() for line in infile)
            lines = (line.split("\n") for line in stripped if line)
            for line in lines:
                split_lines = (l.split(",") for l in line if l)
                for s in split_lines:
                    if s[2] == "OPEN":
                        opened_times += 1

            # print the details that will be saved to the json file:
            print(f"The file: {initial_file_name} was opened: {opened_times} times.\n" +
                  f"The last time it was opened on: {last_date[0]} was at: {last_date[1]}.")
            # format the data which is going to be saved as json:
            json_data = {
                initial_file_name: {
                    "count": opened_times,
                    "last_time_opened": (last_date[0] + " " + last_date[1])
                }
            }
            # write the data:
            outfile.write(json.dumps(json_data))


with Logger('log.txt') as file:
    print(file.read())

Logger.file_to_csv('log.txt', 'log.csv')
Logger.log_file_details('log.csv', 'log.json')
