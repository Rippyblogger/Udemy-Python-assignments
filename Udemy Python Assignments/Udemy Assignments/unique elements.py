def unique(a):
    myset = set(a)
    newlist = list(myset)
    return newlist

result = unique([1,1,1,1,2,2,3,3,3,3,4,5])
print(result)