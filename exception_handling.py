names_tuple = 'Rod', 'Jane', 'Freddy'

try:
    print("###### TRY ######")
    print("The TRY block attempts to run")

    #Prints the tuple as it was originally defined
    print(f"Original Tuple: {names_tuple}")

    #using the 'sorted' function to sort the tuple alphabetically.
    #The 'sorted' function returns a list, not a tuple
    names_sorted_as_list = sorted(names_tuple)
    print(names_sorted_as_list)

    #using the 'append' method to add in an extra item to the list.
    #The 'append' method can only add one item at a time, this is always added to the end of the list.
    names_sorted_as_list.append("Bungle")
    print("Added Bungle:", names_sorted_as_list)

    print("Attempt to manipulate the tuple...")
    #Tuples are immutable and so you are unable to change elements.
    #This will result in a 'TypeError'
    names_tuple[0] = 'Zippy'
    #As the above will cause an error this statement will not be carried out.
    print("Is this code reached?")

#The except blocks are for handling errors.
#This except block will not happen as there is no file handling.
except FileNotFoundError as error:
    print("###### EXCEPT: FileNotFoundError ######")
    print("The EXCEPT / CATCH block only runs if this error happens")
    print(f"The following file can not be found: {error.filename}. Please try another file")

#This block will catch the 'typeerror' that is caused by trying to modify the tuple.
except TypeError as error:
    print("###### EXCEPT: TypeError ######")
    print("Oh dear, that is not allowed on that type")
    print(error)

#This block is for catching any errors that have not already been defined as above.
#The 'typeerror' has been caught by the above exception block and so will catch any other errors that might happen.
except Exception as error:
    print("###### EXCEPT: Exception ######")
    print("Generic catch-all except / catch block")
    print(error)

#This block will always run.
finally:
    # Always close file handle after use
    print("The FINALLY block ALWAYS runs")
    print("The finally block is used to tidy up")
    #this sets names_tuple to none however this is not needed as a tuple wasn't' changed as they are immutiable.
    if names_tuple:
        names_tuple = None

print("After exception handling is finished...the program can continue")
