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

f1(f)   #Functions can be treated as objects and passed along

# Output here is nothing :  Or maybe <object>

f1(f)()

""" Output here is :
Wrapper started
I'm the original function. Hello!
Wrapper ended
"""
f = f1(f)

f()

"""
Output here is :
Wrapper started
I'm the original function. Hello!
Wrapper ended
"""

#Now say I have a wrapper :  x = f1(f) as line 29, then I can use something called Decorator.

print("Decorator !")
def f1(func):
    def wrapper():
        print("Wrapper 2 started")
        func()
        print("Wrapper 2 ended")

    return wrapper

@f1        # similar to f = f1(f)
def f():
    print("I'm the original function. Hello!")

    #Above thing means everytime we call f, it's actually going to call f1

f()
"""
Wrapper 2 started
I'm the original function. Hello!
Wrapper 2 ended
"""

################################################################

print("Decorator with function of arguments !")
def f1(func):
    def wrapper(*args, **kwargs):
        print("Wrapper 2 started")
        func(*args, **kwargs)
        print("Wrapper 2 ended")

    return wrapper

@f1        # similar to f = f1(f)
def f(a):
    print("I'm the original function. Hello!")
    print(a)

f("Here here")
"""
Decorator with function of arguments !
Wrapper 2 started
I'm the original function. Hello!
Here here
Wrapper 2 ended
"""

#################################################

print("Return values within wrappers !")

def f1(func):
    def wrapper(*args, **kwargs):
        print("Wrapper 3 started")
        val = func(*args, **kwargs)   #this will store the value of function which we can return later
        print("Wrapper 3 ended")
        return val

    return wrapper

@f1
def add(x,y):
    return (x+y)

print(add(4,5))

"""
Wrapper 3 started
Wrapper 3 ended
9
"""

