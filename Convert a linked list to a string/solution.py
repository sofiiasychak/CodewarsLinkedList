class Node:
    """
    Class of given linked list.
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(node):
    """
    Solution implementation.
    """
    current_node = node
    next_node = current_node.next
    list_of_data = []

    while next_node is not None:
        list_of_data.append(current_node.data)
        current_node = next_node
        next_node = current_node.next
    list_of_data.append(current_node.data)
    list_of_data.append(None)

    return " -> ".join(map(str, list_of_data))