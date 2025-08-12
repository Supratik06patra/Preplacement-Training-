class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        if not head:
            new_node.next = new_node
            return new_node

        curr = head

        while True:
            if curr.data <= data <= curr.next.data:
                break

            if curr.data > curr.next.data:
                if data >= curr.data or data <= curr.next.data:
                    break

            curr = curr.next

            if curr == head:
                break

        new_node.next = curr.next
        curr.next = new_node

        if data < head.data:
            return new_node
        else:
            return head