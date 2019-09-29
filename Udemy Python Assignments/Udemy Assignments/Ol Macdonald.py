def OldMacdonald(a):
    name = a.capitalize()
    namelist = [x for x in name]
    firstpart = namelist[0:4]
    joinedfirstpart = ''.join(firstpart)
    secondpart = namelist[3:]
    joinedstring = ''.join(secondpart)
    joinedsecondpart = joinedstring.capitalize()
    finalstring = joinedfirstpart +joinedsecondpart
    return finalstring
result = OldMacdonald("supercalifra")

print(result)