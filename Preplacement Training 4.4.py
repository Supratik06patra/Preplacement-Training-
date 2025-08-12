class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def insertAtPosition(last, data, pos):
    if last is None:
        if pos != 1:
            print("Invalid position!")
            return last
        new_node = Node(data)
        last = new_node
        last.next = last
        return last

    new_node = Node(data)

    curr = last.next

    if pos == 1:
        new_node.next = curr
        last.next = new_node
        return last

    for i in range(1, pos - 1):
        curr = curr.next

        if curr == last.next:
            print("Invalid position!")
            return last

    new_node.next = curr.next
    curr.next = new_node

    if curr == last:
        last = new_node

    return last

def print_list(last):
    if last is None:
        return

    head = last.next
    while True:
        print(head.data, end=" ")
        head = head.next
        if head == last.next:
            break
    print()

if __name__ == "__main__":
    first = Node(2)
    first.next = Node(3)
    first.next.next = Node(4)

    last = first.next.next
    last.next = first

    print("Original list: ", end="")
    print_list(last)

    data = 5
    pos = 2
    last = insertAtPosition(last, data, pos)
    print("List after insertions: ", end="")
    print_list(last)