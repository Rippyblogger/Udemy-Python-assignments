def ask(a):
    #int(input("Enter a number: "))
    while True:
        try:
            a=int(input("Enter a number: "))
            print(a**2)
        except:
            print("Please enter an integer")
        else:
            print("Thank you.")
            break


result = ask(2)
print(result)