def panagram(a):
    import string
    b = a.lower()
    b =b.replace(' ','')
    alphabets = list(string.ascii_lowercase)
    newlist = [x for x in b]
    newlist.sort()
    alphabets.sort()
    return alphabets
    for i in alphabets:
        if i in newlist:
            return True
        else:
            return False



result = panagram("The quick brown fox jumps over the lazy dog")
print(result)