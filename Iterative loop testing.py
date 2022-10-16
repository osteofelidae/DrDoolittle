import string
import time

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


numlist = [0]
for number in range(999999999999):
    outstr = ""
    for index in numlist:
        outstr += string.ascii_lowercase[index]
    print(outstr)
    if outstr == "dog":
        while True:
            print("yes")
    if numlist[-1] == 25:
        numlist[-1] = 0
        carry = True
    else:
        numlist[-1] += 1
        carry = False
        
    reference = len(numlist)-2
    while carry == True:
        if reference >= 0:
            if numlist[reference] < 25:
                numlist[reference] += 1
                carry = False
            else:
                numlist[reference] = 0
                carry = True
        elif reference < 0:
            numlist.insert(0,0)
            carry = False
        reference -= 1
    