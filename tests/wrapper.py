class Wrapper:
    def __init__(self, data):
        self.data = data

    def __getattr__(self, attr):
        print("Trace: ", attr)
        return getattr(self.data, attr)
