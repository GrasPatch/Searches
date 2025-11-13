import random
def menu():
    
    #Menu for selecting linear or binary search
    Search = input("Would you like to do a linear or a binary search: ")
    if Search == "binary":
        binary()
    elif Search == "linear":
        linear()
    else:
        print("Please enter either linear or binary")

def binary():
    found = False
    
    #Creates a random list with 10000 values and sorts it
    wlist = [random.randint(1, 1000) for x in range (1, 1001)]
    wlist.sort()

    print("this is a binary search(Values 1-1000)")
    
    #Asks the user to input what term they want to search for
    searchterm = int(input("What would you like to search for :"))
    
    #Assigns the first and last variables
    first = 0
    last = len(wlist) - 1

    #Finds the searchterm
    while(found == False and last >= first):
        mid = (first+last)//2

        if(searchterm == wlist[mid]):
            found = True
            break
        elif(searchterm > wlist[mid]):
            first = mid+1

        elif(searchterm < wlist[mid]):
            last = mid-1
            
    #Outputs whether the term was found and what position it was in
    if found == True:
        print("Found", searchterm, "at position", mid)

    else:
        print("Couldn't find", searchterm)


def linear():
    
    #Creates a random list with 100 values
    nlist = [random.randint(1, 100) for x in range (1, 101)]
    print("This is a linear search(Values 1-100)")
    
    #Asks the user to input what term they want to search for
    searchterm = int(input("What would you like to search for :"))

    #Searches for the term
    found = 0
    for i in range (len(nlist)):
        if searchterm == i:
            found+=1

    #Outputs whether the term was found
    if found != 0:
        print("Found", searchterm)
    else:
        print("Couldn't find", searchterm)
        
menu()

