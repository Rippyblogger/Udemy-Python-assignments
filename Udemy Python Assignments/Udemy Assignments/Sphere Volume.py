def spherevol(r):
    pi = 3.14
    div = 4/3
    spherevolume = div * pi * (r**3)
    return  spherevolume

result = spherevol(2)
print(result)