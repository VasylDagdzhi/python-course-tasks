from datetime import datetime


def timer(function):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = function(*args, **kwargs)
        end = datetime.now()
        print(
            "Function executed: {time.seconds}s {time.microseconds}m time.".format(
                time=end - start
            )
        )
        return result

    return wrapper
