def rangecheck(num,low,high):
    if num in range(low,high+1):
        return True
    else:
        return False

result = rangecheck(5,3,9)
print (result)