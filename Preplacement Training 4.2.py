class Solution:
    def delete_node(self, head, x):
        if head is None:
            return None

        if x == 1:
            new_head = head.next
            if new_head:
                new_head.prev = None
            head = None  
            return new_head

        curr = head
        count = 1
        while curr and count < x:
            curr = curr.next
            count += 1

        if curr is None:
            return head

        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev

        curr = None

        return head