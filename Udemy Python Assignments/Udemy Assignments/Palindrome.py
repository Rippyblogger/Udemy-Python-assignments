def palindrome(s):
    list1 = [x for x in s]
    list2 = list1[::-1]
    if list1 == list2:
        return True
    else:
        return False

result = palindrome('helleh')
print (result)