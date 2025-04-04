class Node(object):
    """
    Given class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """
    Solution implementatin.
    """
    new_node = Node(data)

    if head is None:
        return new_node

    if data < head.data:
        new_node.next = head
        return new_node

    current = head
    if current.next:
        if current.next.data < data:
            current = current.next

            if current.next:
                if current.next.data < data:
                    current = current.next

                    if current.next:
                        if current.next.data < data:
                            current = current.next

    new_node.next = current.next
    current.next = new_node
    return head
