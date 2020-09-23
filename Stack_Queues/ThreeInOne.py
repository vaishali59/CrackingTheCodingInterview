class FixedMultiStack:
    def __init__(self,stacksize,n):
        self.stackcapacity = stacksize
        self.numofstacks = n
        self.array = [0]*(self.numofstacks*self.stackcapacity)
        self.size =[0]*self.numofstacks

    def __str__(self):
        return str(self.array)

    def push(self,stacknum,value):
        if self.isFull(stacknum):
            raise Exception("{} stack is full".format(stacknum))
        topindex = self.topIndex(stacknum)
        self.array[topindex] = value
        self.size[stacknum]+=1

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception("{} stack is empty".format(stacknum))
        else:
            topfullidx = self.topIndex(stacknum) - 1
            value = self.array[topfullidx]
            self.array[topfullidx] = 0
            self.size[stacknum] -= 1
            return value

    def peek(self,stacknum):
        if self.isEmpty(stacknum):
            raise Exception("{} stack is empty".format(stacknum))
        else:
            topfullidx = self.topIndex(stacknum) - 1
            return self.array[topfullidx]

    def isFull(self,stacknum):
        return self.size[stacknum] == self.stackcapacity

    def topIndex(self,stacknum):
        offset = stacknum*self.stackcapacity
        currsize = self.size[stacknum]
        idx = offset + currsize
        return idx
    
    def isEmpty(self,stacknum):
        return self.size[stacknum] == 0
            
obj = FixedMultiStack(4,3)
obj.push(0,"a")
obj.push(1,"A")
obj.push(2,100)
print(obj)
obj.push(0,"b")
obj.push(1,"B")
obj.push(2,200)
print(obj)
print(obj.peek(2))
print(obj.pop(0))
print(obj)
