# Input list L with unlimited numbers
# Stop when type 'stop'
# Sort the list

from calendar import c


L = []
print("---")
print("Type 'stop' when done")
print("---")
p = 1
while True:
    # Define what suffix for each ordinal number
    k = ['st','nd','rd','th']
    if p%10 in [1,2,3] and p%100 not in [11,12,13]:
        i = p%10 - 1
    else:
        i = 3
    val = input(str(p) + k[i] + " number: ")

    # Check if the input is valid (is numeric)
    if val.isnumeric():
        val = float(val)
        p += 1
        L.append(val)
    else:
        if val == 'stop':
            break
        else:
            print("Error! The list must only contain numeric values.\nPlease re-enter the " + str(p) + k[i] + " value!")
            continue   
print("The original list: " + str(L))

# Find Min
def findMin(L,startIndx):
    m = L[startIndx]
    idx = startIndx
    for i in range(startIndx,len(L)):
        x = L[i]
        if x < m:
            m = x
            idx = i
            c += 1
    return m
print(findMin(L))

