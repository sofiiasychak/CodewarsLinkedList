class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def get_nth(node, index):
    """
    Implementation of solution.
    """
    if node is None:
        raise IndexError

    current_node = node
    count = 1

    while current_node:
        if count == index:
            return current_node
        current_node = current_node.next
        count += 1
    raise IndexError