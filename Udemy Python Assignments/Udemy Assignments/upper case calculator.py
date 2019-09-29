def uppercalc(strin):
    uppercount = 0
    lowercount = 0
    import string
    eggs = list(string.ascii_uppercase)
    for i in strin:
        if i == i.upper() and i in eggs:
            uppercount +=1
        elif i == i.lower():
            lowercount +=1
        else:
            continue
    return "No. of upper case characters = "+str(uppercount)+ " While no. of lower case characters = " + str(lowercount)


result = uppercalc('Hello Mr. Rogers, how are you this fine Tuesday?')
print(result)