def master_yoda(a):
    newlist = [x for x in a]
    #return newlist
    finallist = newlist[::-1]
    #return finallist
    newstring = ''.join(finallist)
    return newstring

result = master_yoda("The boy is good")
print(result)
