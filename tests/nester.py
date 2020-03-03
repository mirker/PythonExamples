'''
def generate():
    class Spam:
        count  = 1
        def method(self):
            print(Spam.count)
    return Spam()
'''
def generate():
    class Spam:
        count = 1
        def method(self):
            print(self.__class__.count)
    return Spam()
generate().method()
