def find33(a):
    for i in range(0, len(a)-1):
        if a[i] == 3 and a[i + 1] == 3:
            return "True"
        else:
            return "No consecutive integers equal 3"


    #if a[0]==3 and a[a+1]==3:
     #   return "True"
    #else:
     #   return "No consecutive integers equal 3"

result = find33([1,2,3,3,4,5,6])
print (result)