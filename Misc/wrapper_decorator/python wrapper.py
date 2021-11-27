print(" Examples ")
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

import datetime

dt = datetime.date.today()
now = datetime.datetime.now()

print(dt)
print(now)

print("We design a logger function to keep track of run function \n")

def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
             f.write("Called function with "+" ".join([str(arg) for arg in args])+" at "+str(now)+"\n")
             val = func(*args,**kwargs)
             print(val)
             return val

    return wrapper

@log
def run(a,b,c=10):
    print(a+b+c)

run(1,3,c=10)

"""
 Examples 
Decorator !
2021-04-12
2021-04-12 22:25:35.947062
We design a logger function to keep track of run function 

14
None
"""