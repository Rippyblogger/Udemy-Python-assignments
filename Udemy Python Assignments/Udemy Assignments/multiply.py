def multiply(a):
    count = 1
    for i in a:
        if i:
            count = count * i
        else:
            break
    return count

result = multiply([1,2,3,-4])
print(result)
