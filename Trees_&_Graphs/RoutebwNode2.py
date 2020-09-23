from collections import defaultdict
class node:
    def __init__(self,val):
        self.val = val
        self.edges = []

    def __repr__(self):
        return ("{}".format(self.val))

class graph:
    def __init__(self):
        self.d = defaultdict(node)

    def __str__(self):
        return str(self.d.values())

    def connect(self,a,b):
        if a!=None and b!=None:
            nodeA = self.d.get(a,None)
            if not nodeA:
                nodeA = node(a)
                self.d[a] = nodeA
            nodeB = self.d.get(b,None)
            if not nodeB:
                nodeB = node(b)
                self.d[b] = nodeB
            
            nodeA.edges.append(nodeB)
            

    def haveRoute(self,s,e):
        nodeS = self.d.get(s,None)
        nodeE = self.d.get(e,None)
        if not nodeS or not nodeE:
            return False

        q=[nodeS]
        visited = set()
        while q:
            node = q.pop(0)
            for n in node.edges:
                if n == nodeE:
                    return True
                if n not in visited:
                    q.append(n)
            visited.add(node)
        return False

g = graph()
g.connect(0,1)
g.connect(1,2)
g.connect(2,3)

print(g)
print(g.haveRoute(2, 0))
print(g.haveRoute(0, 3))
