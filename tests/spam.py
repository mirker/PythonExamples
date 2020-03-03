class Spam:
    NumberOfInstance = 0
    def __init__(self):
        Spam.NumberOfInstance += 1

    def PrintInstanceNum():
        print("Number of instance: ", Spam.NumberOfInstance)

    PrintInstanceNum = staticmethod(PrintInstanceNum)

class Sub(Spam):
    def PrintInstanceNum():
        print("Extra stuff...")
        Spam.PrintInstanceNum()

    PrintInstanceNum = staticmethod(PrintInstanceNum)
