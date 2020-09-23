class StackMin:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size =0
        self.arr =[]
        self.mini = float('inf')
        self.d={}

    def __str__(self):
        return str(self.arr)

    def push(self,value):
        if not (type(value) is int or type(value) is float):
            raise Exception("Numeric Values Only")
        if self.isFull():
            raise Exception("stack is full")
        self.arr.append(value)
        self.size += 1
        self.adjustmin(value)

    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty")
        value = self.arr[self.size - 1]
        del self.arr[self.size - 1]
        self.size -= 1
        self.adjustmin(value)
        return value

    def min(self):
        return self.mini

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def adjustmin(self,value):
        if value == self.mini:
            self.mini = self.d[value]
            del self.d[value]
        elif value < self.mini:
            self.d[value] = self.mini
            self.mini = value
        
        
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
