class Solution:
    def reverseDLL(self, head):
        if head is None or head.next is None:
            return head

        curr = head
        temp = None

        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev  

        
        if temp:
            head = temp.prev

        return head

