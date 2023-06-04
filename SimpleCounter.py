class SimpleCounter:
    __secretCount = 0       #Private Variable
    publicCount = 0         #Public Variable

    def count(self):
        self.__secretCount +=100
        print(self.__secretCount)

counter = SimpleCounter()
counter.count()
print(counter.publicCount)