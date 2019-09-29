class ErrorTry:
    def __init__(self,name):
        self.name = name

    @classmethod
    def from_input(cls):
        return cls(
            input("name: "),
    )


    def Error1(self):

        while True:
            try:
                a = input("a:")
                b = input("b:")
                c = input("c:")
                for i in ['a','b','c']:
                    print(i**2)
            except TypeError:
                print("There was a type error")
            except:
                print("Error")
            else:
                print("All done.")
            finally:
                print("Done")

Something = ErrorTry.from_input()
Something.Error1()


