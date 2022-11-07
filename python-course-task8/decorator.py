def timer(function):
    def wrapper(*args, **kwargs):
        print(f"Function: {function.__name__}")
        result = function(*args, **kwargs)
        return result

    return wrapper
