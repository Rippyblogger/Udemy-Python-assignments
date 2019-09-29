def Arraysum(*args):
    #newlist = [x for x in args]
    for i in args:
        if args[i:i+3] ==[0,0,7]:
            return True
        else:
            return False


result = Arraysum(4,5,6,7,8,0,0,7)
print(result)