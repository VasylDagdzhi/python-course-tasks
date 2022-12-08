import logging

print("Part 1.\n")


# # 1. double_result
# # This decorator function should return the result of another function multiplied by two
def double_result(func):
    # return function result multiplied by two
    def inner(*args, **kwagrs):
        result = func(*args, **kwagrs)
        return result * 2

    return inner


def add(a, b):
    return a + b


print(f"Result of adding 5 and 5 is: {add(5, 5)}")  # 10


@double_result
def add(a, b):
    return a + b


print(f"Result of adding 5 and 5 with double decorator is: {add(5, 5)}")  # 10

#
#
# # 2. only_odd_parameters
# # This decorator function should only allow a function to have odd numbers as parameters,
# # otherwise, return the string "Please use only odd numbers!"
#

print("\nPart 2.1 Adding\n")


def only_odd_parameters(func):
    def inner(*args, **kwargs):
        print(f"Result with odd numbers: {args.__str__()} is: ")
        for arg in args:
            if arg % 2 == 0:
                raise ValueError("Please use only odd numbers here.")
        result = func(*args, **kwargs)
        return result

    return inner


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))  # 10
try:
    print(add(4, 4))  # "Please use only odd numbers!"
except ValueError as e:
    print(e)


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print("\nPart 2.2 Multiplying\n")
print(multiply(3, 5, 7, 9, 9))  # 10
try:
    print(multiply(2, 4, 8, 6, 5))  # "Please use only odd numbers!"
except ValueError as e:
    print(e)

print("\nPart 3 Logging\n")

#
#
# # 3.* logged
# # Write a decorator which wraps functions to log function arguments and the return value on each call.
# # Provide support for both positional and named arguments (your wrapper function should take both *args
# # and **kwargs and print them both):
#

logging.basicConfig(filename='logs/function_execution.log', format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S", level=logging.INFO)


def logged(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if args.__len__() > 0:
            if kwargs.__len__() > 0:
                logging.info(f"Function: {func.__name__} ({args}{kwargs}) executed and returned: {result}")
            else:
                logging.info(f"Function: {func.__name__} ({args}) executed and returned: {result}")
        else:
            logging.info(f"Function: {func.__name__} ({kwargs}) executed and returned: {result}")
        return result

    # log function arguments and its return value
    return inner


@logged
def func(*args, **kwargs):
    if args.__len__() > 0:
        if kwargs.__len__() > 0:
            return 3 + len(args) * len(kwargs)
        else:
            return 3 + len(args)
    elif kwargs.__len__() > 0:
        return 2 + len(kwargs)


# you called func(4, 4, 4)
# # it returned 6
func(4, 4, 4)
func(a=1, b=2, c=3)
func(2, 3, afg=4, num=9)

# # 4. type_check
# # you should be able to pass 1 argument to decorator - type.
# # decorator should check if the input to the function is correct based on type.
# # If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.
#
# def type_check(correct_type):
#     # put code here
#     pass
#
#
# @type_check(int)
# def times2(num):
#     return num * 2
#
#
# print(times2(2))
# times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function
#
#
# @type_check(str)
# def first_letter(word):
#     return word[0]
#
#
# print(first_letter('Hello World'))
# first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function
