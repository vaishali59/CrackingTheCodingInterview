# Remove Duplicates from Linked List

class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)+"-->"+str(self.next)

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def add(self,list1):
        for element in list1:
            if not self.head:
                self.head = Node(element)
                curr = self.head
            else:
                curr.next = Node(element)
                curr = curr.next
                               
    def __str__(self):
        return str(self.head)


list1 = [1,1,1]

l = LinkedList()
l.add(list1)
print(l)
"""
def removeDuplicates(linkedlist):
    visited = set()
    h = head = linkedlist.head
    prev = Node()
    prev.next = head
    while head:
        if head.val not in visited:
            visited.add(head.val)
            prev = head
        else:
            prev.next = head.next
        head = head.next
    return h
"""
#when no temp buffer is available
def removeDuplicates(l):
    h = curr = l.head
    while curr:
        runner = curr.next
        prev = curr
        while runner:
            if runner.val == curr.val:
                prev.next = runner.next
            else:
                prev = prev.next
            runner = runner.next
        curr = curr.next
    return h
print(removeDuplicates(l))
