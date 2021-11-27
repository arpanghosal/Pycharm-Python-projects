# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def f1(func):
    def wrapper():
        print("Wrapper started")
        func()
        print("Wrapper ended")

    return wrapper

def f():
    print("I'm the original function. Hello!")

f1(f)