class Solution:    
    def pairWiseSwap(self, head):
        if head is None or head.next is None:
            return head

        new_head = head.next

        prev = None
        curr = head

        while curr and curr.next:
            first = curr
            second = curr.next
            next_pair = second.next

            
            second.next = first
            first.next = next_pair

            if prev:
                prev.next = second

            prev = first
            curr = next_pair

        return new_head