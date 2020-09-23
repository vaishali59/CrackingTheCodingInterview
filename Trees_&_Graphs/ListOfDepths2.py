class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        string =""
        if not self.val:
            return
        string+=str(self.val)
        string+=" "
        if self.left:
            string+=str(self.left)
        string+=" "
        if self.right:
            string+=str(self.right)
        return string

root = Node(5)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(20)
root.left.right = Node(25)
root.right.left = Node(30)
root.right.right = Node(35)
print(root)

class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)+"--->"+str(self.next)


def listOfDepths(root):
    if not root:
        return None
    res =[]
    q = [root]
    while q:
        length = len(q)
        #print("{}:{}".format(q,length))
        prev = ListNode()
        for i in range(length):
            node = q.pop(0)
            #print("Queue Node : {}".format(node))
            nn = ListNode(node.val)
            #print("ListNode : {}".format(nn))
            #print(prev)
            if not prev.val:
                prev = nn
                head = prev
            else:
                prev.next = nn
                prev = nn
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(head)
    return res

res = listOfDepths(root)
for node in res:
    print(node)
