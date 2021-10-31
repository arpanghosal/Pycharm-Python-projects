# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def create_tuple():
    myTuple = tuple(["Arpan",26, "Delhi"])
    print(myTuple)   #('Arpan', 26, 'Delhi')
    print(myTuple[0])   #Arpan
    return myTuple
def check_tuple():
    x = create_tuple()
    if "Tin" in x:
        print("ye")
    else:
        print("no")
    if "Delhi" in x:
        print("ye")
    else:
        print("no")
    print(x.count('Arpan')) #1
    print(x.index('Arpan'))  #0


#Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    create_tuple()
    check_tuple()
    myTuple  = create_tuple()
    myList = list(myTuple)
    print(myList)  # ['Arpan', 26, 'Delhi']
    print(myList[-1])  # Delhi
    reverseTuple = myTuple[::-1]   #Start from beginning, stop at end, but in steps of -1 so reversed
    print(reverseTuple)  #('Delhi', 26, 'Arpan')
    myTuple = (1,2,3,4,5,6,7)
    #Storing elements from tuple
    i1, *i2, i3 = myTuple
    print(i1)  #first item
    print(i2)
    print(i3)   #Last item

    #Tuples are more convenient than lists when comes to processing time and memory space
     # TODO: Add more from the data camp


