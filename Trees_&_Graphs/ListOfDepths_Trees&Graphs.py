class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        string =""
        if not self.val:
            return
        if self.left:
            string+=str(self.left)
        string+=" "
        string+=str(self.val)
        string+=" "
        if self.right:
            string+=str(self.right)
        return string
    
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        self.last = self

    def __str__(self):
        return str(self.val) + "--->" + str(self.next)
    
    def add(self,val):
        newNode = ListNode(val) 
        self.last.next = newNode
        newNode.prev = self.last
        self.last = newNode

    def remove(self):
        curr = self.last
        self.last = self.last.prev
        self.last.next = None
    
root = Node(5)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(20)
root.left.right = Node(25)
root.right.left = Node(30)
root.right.right = Node(35)
print(root)

def func(root):
    if not root:
        return None
    res = []
    queue = [root]
    level =0
    
    while queue:
        res.append(ListNode(0))
        length = len(queue)
        for i in range(length):
            root = queue.pop(0)
            res[level].add(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        level+=1

    for node in res:
         print(node.next)

func(root)
