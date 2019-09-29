def master_yoda(a):
    newlist = [x for x in a]
    finallist = newlist[-1::1]
    newstring = ''.join(finallist)
    return newstring

result = master_yoda("The boy is good")
print(result)
