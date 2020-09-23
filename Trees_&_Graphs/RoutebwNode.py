from collections import defaultdict
class graph:
    def __init__(self):
        self.d = defaultdict(list)
        
    def connect(self, a, b):
        self.d[a].append(b)

    def haveRoute(self, src, dest):
        if src == dest:
            return True
        q=[src]
        visited = set()
        #visited.add(src)

        while q:
            node = q.pop(0)
            if node == dest:
                return True
            for nei in self.d[node]:
                if nei not in visited:
                    q.append(nei)
                    #visited.add(nei)
            visited.add(node)
        return False

g = graph()
g.connect(0,1)
g.connect(1,2)
g.connect(2,3)
g.connect(3,None)

#g = {0:[1], 1:[2], 2:[3], 3:[]}

print(g.haveRoute(2, 0))
print(g.haveRoute(0, 3))
