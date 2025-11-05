# Binary search

import random

# Sorted list
wlist = [random.randrange(1, 1001) for x in range(1000)]
wlist.sort()

found = False
searchTerm = int(input("Intput an iteger to search for: "))

# first and last pointers
first = 0
last = len(wlist) - 1

# searches list for searchTerm
while (found == False and last >= first):
    mid = (first + last) // 2

    if (searchTerm == wlist[mid]):
        found = True
        break

    elif (searchTerm < wlist[mid]):
        last = mid - 1

    elif (searchTerm > wlist[mid]):
        first = mid + 1

# prints if it was found and its found position in the list
if found == True:
    print("Found", searchTerm, "at position", mid)

else:
    print("Couldn't find", searchTerm)
        
