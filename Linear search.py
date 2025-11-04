# Linear search
nlist = [1, 58, 69, 420, 345, 293, 32, 97]
found = False

searchTerm = int(input("Enter a term to search for: "))

for x in range(len(nlist)):

    if (searchTerm == nlist[x]):

        found = True

if (found == True):

     print("Found", searchTerm)

else:

    print("Couldn't find", searchTerm)
