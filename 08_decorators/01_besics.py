from functools import wraps
def my_decorators(func):
    @wraps(func)
    def wrapper():
        print("Before function runes")
        func()
        print("After function runes")
    return wrapper

@my_decorators
def greet():
    print("Hello from decorators class from Hitesh sir")

greet()
print(greet.__name__)