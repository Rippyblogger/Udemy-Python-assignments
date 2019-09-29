def countprimes(a):
    newlist = [x for x in range(a + 1)]
    count = 0
    del newlist[0:2]
    for i in newlist:
        if a%i==0:
            count += 1
    return count

result = countprimes(10)
print(result)