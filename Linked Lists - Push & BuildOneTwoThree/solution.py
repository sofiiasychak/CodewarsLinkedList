class Node:
    """
    Class of given linked list.
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def push(head, data):
    """
    Solution of 1 func.
    """
    return Node(data, head)

def build_one_two_three():
    """
    Solution of 2 func.
    """
    return Node(1, Node(2, Node(3)))
