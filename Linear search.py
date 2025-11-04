import random

# Linear search
nlist = [random.randrange(1, 101) for x in range(1000)]
found = False

# User enters data item
searchTerm = int(input("Enter a term to search for: "))

# Searches nlist until it finds data item

Positions = []
Found = 0
for i in range(0, len(nlist)):
    if nlist[i] == searchTerm:
        Found += 1
        Positions.append(str(i)+",")
        
if (Found != 0):
    print("Found", searchTerm, "in", "".join(Positions))

else:
    print("Couldn't find", searchTerm)

