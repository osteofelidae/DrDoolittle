import string
import time

mainlist = [0]

for x in range (9999999999999):
    outstr = ""
    time.sleep(0.01)
    numlist = []
    exponent = 1
    samplenum = x
    while 26**exponent < x:
        exponent += 1
    exponent -= 1
    while exponent >= 0:
        print(samplenum/(26**exponent))
        numlist.append(int(samplenum/(26**exponent)))
        samplenum = samplenum % (26**(exponent))
        exponent -= 1
    for item in numlist:
        print(item)
        outstr += str((string.ascii_lowercase[item]))
    print(outstr)