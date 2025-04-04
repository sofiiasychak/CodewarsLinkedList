class Node:
    """
    Class of given linked list.
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    """
    Solution implementation.
    """
    if s in ("None", "null"):
        return None

    splitted_string = s.split(" -> ")
    node = None
    for i, node_data in enumerate(splitted_string[:-1][::-1]):
        if i == 0:
            node = Node(int(node_data), None)
        else:
            node = Node(int(node_data), node)
    return node
