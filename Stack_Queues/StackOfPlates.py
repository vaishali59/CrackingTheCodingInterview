class StackOfPlates:
    def __init__(self,threshold):
        self.subcapacity = threshold
        self.substacks =[]

    def __str__(self):
        return str(self.substacks)
    
    def push(self,value):
        if self.isEmpty() or self.isFull():
            self.substacks.append([])
        self.substacks[-1].append(value)

    def pop(self):
        if self.isEmpty():
            raise Exception("Whole set empty")
        value = self.__pop()
        return value

    def __pop(self):
        laststack = self.substacks[-1]
        val = laststack.pop()
        if len(laststack)==0:
            self.substacks.pop()
        return val

    def isEmpty(self):
        return len(self.substacks) == 0

    def isFull(self):
        if self.substacks and len(self.substacks[-1]) == self.subcapacity:
            return True
        return False

set1 = StackOfPlates(4)
set1.push(10)
set1.push(20)
set1.push(100)
set1.push(200)
print(set1.pop())
print(set1.pop())
print(set1)
print(set1.pop())
print(set1)
print(set1.pop())
print(set1)
print(set1.pop())
print(set1)
