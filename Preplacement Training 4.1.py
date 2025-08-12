class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def sortedInsert(self, head, x):
        new_node = Node(x)

        if head is None:
            return new_node
        if x < head.data:
            new_node.next = head
            head.prev = new_node
            return new_node

        curr = head
        while curr.next is not None and curr.data < x:
            curr = curr.next

        if x <= curr.data:
            prev_node = curr.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = curr
            curr.prev = new_node
        else:
