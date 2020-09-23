import copy

class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

    def __str__(self):
        string =""
        if not self.val:
            return
        if self.left:
            string+=str(self.left)+" "
        string+=str(self.val)
        if self.right:
            string+=" " + str(self.right)
        return string

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self,val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(val,self.root)

    def _insert(self,val,node):
        if val < node.val:
            if not node.left:
                node.left = Node(val)
            else:
                self._insert(val,node.left)
        else:
            if not node.right:
                node.right = Node(val)
            else:
                self._inser(val,node.right)

    def __str__(self):
        return str(self.root)

def weaveLists(left,right,prefix,weaved):
    if not left or not right:
        weaved.append(prefix + left + right)
        return weaved

    headleft = left.pop(0)
    prefix.append(headleft)
    weaveLists(left,right,prefix,weaved)
    prefix.pop()
    left.insert(0, headleft)

    headright = right.pop(0)
    prefix.append(headright)
    weaveLists(left,right,prefix,weaved)
    prefix.pop()
    right.insert(0, headright)

def bstSequences(root):
    res=[] 
    if not root:
        res.append([])
        return res
    
    prefix = [root.val]
    leftseq = bstSequences(root.left)
    rightseq = bstSequences(root.right)

    for l1 in leftseq:
        for l2 in rightseq:
            weaved =[]
            weaveLists(l1,l2,prefix,weaved)
            res+= weaved
    return res


if __name__ == "__main__":
    tree = Tree()
    
    tree.insert(20)
    tree.insert(10)
    tree.insert(25)
    tree.insert(5)
    tree.insert(15)
    #print(tree.getRoot().left)
    
    allseq = bstSequences(tree.getRoot())

    for each in allseq:
        print(each)

    print(len(allseq))
