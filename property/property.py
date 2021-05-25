#!/usr/bin/env python3   
import sys   #to read inline arguments

print("Hello there\n")
print(str(sys.argv))   

print(sys.argv[1])  #prints out all arguments being entered including 0th as the file name

#########Property #########


class House:
    def __init__(self,price):
        self._price = price  #The variable is 'protected' and can't be called outside class

    @property    #This assigns the values, getter functionality
    def price(self):
        print("\nGetter being called\n")
        return self._price


    @price.setter   #price is our property, so we use it with setter functionality
    def price(self, new_price):
        print("\nWell now you called the Setter\n")
        if new_price > 100 and isinstance(new_price,int):
            self._price = new_price
        else:
            print("\nHmmmm, something's wrong!")

    @price.deleter
    def price(self):
        print("\nTime for Deleter\n")
        del self._price


house_g =  House(sys.argv[1])   #Object to class
print(house_g.price)   


house_s = House(sys.argv[1])
house_s.price = int(sys.argv[2])   #need to convert to int or else it is str
print(house_s.price)

house_d = House(sys.argv[1])
del house_d.price
print(house_d.price) #Deleted item is being called, so it will show error
""" 
Output : python property.py 130 1500

Hello there

['property.py', '130', '1500']
130

Getter being called

130

Well now you called the Setter


Getter being called

1500

Time for Deleter


Getter being called

Traceback (most recent call last):
  File "property.py", line 46, in <module>
    print(house_d.price)
  File "property.py", line 19, in price
    return self._price
AttributeError: 'House' object has no attribute '_price'
"""

