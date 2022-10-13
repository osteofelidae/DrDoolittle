import string

mainlist = [0]
print(string.ascii_lowercase[1])
while True:
    mainstr = ""
    index = len(mainlist)-1
    for letter in mainlist:
        mainstr += (string.ascii_lowercase[letter])
    print(mainstr)
    
    if mainlist[index] < 26:
        mainlist[index] += 1
    else:
        carry = False
        for x in range(index):
            if carry == True:
                mainlist[index-x] += 1
            if mainlist[index-x] < 26:
                carry == False
                mainlist[index-x] += 1
            else:
                carry == True
                mainlist[index-x] = 0