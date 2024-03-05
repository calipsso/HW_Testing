import random
import math

class ElementsStorage:
    def __init__(self):
        self.storage = set()
    def randomChoiceInt(self, a, b): # random vstup
        for _ in range(10):
            self.storage.add(random.randint(a, b))
        print(self.storage)

    def userChoiceInt(self): # uzivatelsky vstup
        usrVstup = input("Zadajte 10 cisel oddelenych medzerou: ") # zadaj tieto cisla 1 2 3 4 5 6 7 8 9 10
        for num in usrVstup.split():
            self.storage.add(int(num))
        return self.storage

    #def sumElements(self):
        #sumZoznam = 0
        #for num in self.storage:
            #sumZoznam += num
        #return sumZoznam


class FunctionsElements(ElementsStorage):

    def sumElements(self):
        sumZoznam = 0
        for num in self.storage:
            sumZoznam += num
        return sumZoznam

    def lenStorage(self):
        d = len(self.storage)
        return d

    def arithmElements(self, a, b):
        delenec = b//a
        return delenec

    def minIsGreaterMax(self,a , b):

        if a > b:
            return True
        else:
            return False

    def minElement(self):
        minEl = min(self.storage)
        return minEl
    def maxElement(self):
        maxEl = max(self.storage)
        return maxEl



elements = FunctionsElements()
# elements = ElementsStorage()

elements.randomChoiceInt(10, 99) #random
# elements.userChoiceInt()  # user

# print(elements.storage)
print(elements.sumElements())
print(elements.arithmElements(elements.lenStorage(), elements.sumElements()))
print(elements.maxElement())
print(elements.minElement())
print(elements.minIsGreaterMax(elements.maxElement(), elements.minElement()))