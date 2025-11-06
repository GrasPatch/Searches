import time
import random
nlist = [random.randrange(1, 101) for x in range(10000)]

searchTerm = int(input("What would you like to search for"))

start = time.time()

Found = 0
for i in range(0, len(nlist)):
    if nlist[i] == searchTerm:
        Found += 1

if (Found != 0):
    print("Found item")
else:
    print("Didn't find item")
    
end = time.time()
print(f"Time taken for completion: {end-start} seconds")
