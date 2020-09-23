import random
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.count =1

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val,end=" ")
        if self.right:
            self.right.inorder()

    def insert(self, data):
        if data < self.val:
            if not self.left:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)
        self.count+=1

    def find(self,data):
        if data == self.val:
            return self
        elif data < self.val:
            if not self.left:
                return None
            return self.left.find(data)
        elif data > self.val:
            if not self.right:
                return None
            return self.right.find(data)
        else:
            return None

    def size(self):
        return self.count

    def getNodei(self,i):
        leftsize = self.left.size() if self.left else 0
        if i < leftsize:
            return self.left.getNodei(i)
        elif i == leftsize:
            return self
        else:
            return self.right.getNodei(i-(leftsize+1))

    def minValue(self,node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr
            

    def delete(self, data):
        if self.val == data:
            if not self.left:
                temp = self.right
                self = None
                return temp
            if not self.right:
                temp = self.left
                self = None
                return temp
            else:
                temp = self.minValue(self.right)
                self.val = temp.val
                self.right = self.right.delete(temp.val)
        elif data < self.val:
            self.left = self.left.delete(data)
        else:
            self.right = self.right.delete(data)
        return self
            
root = TreeNode(20)
root.insert(30)
root.insert(35)
root.insert(10)
root.insert(15)
root.insert(17)
root.insert(5)
root.insert(7)
root.insert(3)

root.inorder()    

root.delete(10)
print()
root.inorder()
