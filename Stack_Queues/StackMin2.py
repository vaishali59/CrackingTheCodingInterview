class StackMin:
    def __init__(self,capacity):
        self.capacity = capacity
        self.arr =[]
        self.d=[]

    def __str__(self):
        return str(self.arr)

    def push(self,value):
        if not (type(value) is int or type(value) is float):
            raise Exception("Numeric Values Only")
        if self.isFull():
            raise Exception("stack is full")
        self.arr.append(value)
        if value < self.min():
            self.d.append(value)

    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty")
        value = self.arr.pop()
        if value == self.min():
            self.d.pop()
        return value

    def min(self):
        if not self.d:
            return float('inf')
        else:
            return self.d[-1]

    def isFull(self):
        return len(self.arr) == self.capacity

    def isEmpty(self):
        return len(self.arr) == 0

        
        
stack1 = StackMin(1000)
stack1.push(12)
stack1.push(5)
stack1.push(100)
print(stack1)
print(stack1.min())       
stack1.push(1)
stack1.push(50)
stack1.push(18)
stack1.push(12)
stack1.push(5)
print(stack1)
stack1.pop()
print(stack1)
print(stack1.min())
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
print(stack1)
print(stack1.min())
