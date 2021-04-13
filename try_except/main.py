# This is a sample Python script.

try:
    f = open('filerandom.txt')
    var = var_bad
except FileNotFoundError:
    print('Sorry. The file does not exist')   #This error if the file name is not found
except Exception:
    print('Sorry. Something is wrong')   #This error if anything else

"""
Sorry. The file does not exist
"""
########################### Now the file path is correct ######################
try:
    f = open('file_random.txt')
    var = var_bad
except FileNotFoundError:
    print('Sorry. The file does not exist')   #This error if the file name is not found
except Exception:
    print('Sorry. Something is wrong')   #This error if anything else

"""
Sorry. Something is wrong
"""

##################################  Actual message and not custom ################################

try:
    f = open('file_random.txt')
    var = var_bad
except FileNotFoundError as e:
    print(e)   #This error if the file name is not found
except Exception as e:
    print(e)   #This error if anything else    - this will show the actual error now, not custom print message

"""
name 'var_bad' is not defined
"""
###################### Else pass ################################################

try:
    f = open('file_random.txt')
    #var = var_bad
except FileNotFoundError as e:
    print(e)
except Exception as e:    #if this arises, then it won't go to else statement
    print(e)
else:
    print(f.read())    #just to print out the contents of the file
    f.close()

"""
I am just a random file here.
"""

################### Want to do something anyway never mind the exceptions? Use finally #####
print ("we will jump to finally even if there is exception")
try:
    f = open('filerandom.txt')
    var = var_bad
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Well, finally. Useful for final closures")

"""
we will jump to finally even if there is exception
[Errno 2] No such file or directory: 'filerandom.txt'
Well, finally
"""

############## Raising exceptions on your own ######################

print("we can raise our own exceptions using raise")
try:
    f = open('filerandom.txt')
    if f.name == 'filerandom.txt':
        raise Exception
# except FileNotFoundError as e:
#     print(e)
except Exception as e:
    print('Arrgghh! Error')
else:
    print(f.read())
    f.close()
finally:
    print("Well, finally. Useful for final closures")

"""
we can raise our own exceptions using raise
Arrgghh! Error
Well, finally. Useful for final closures
"""