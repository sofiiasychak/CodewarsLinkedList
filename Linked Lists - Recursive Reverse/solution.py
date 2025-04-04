class Node(object):
    """
    Given class.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """
    Solition of the task.
    """
    if head == None:
        return head
    if not head.next:
        return head

    else:
        new_start = reverse(head.next)
        current = head.next
        current.next = head

        head.next = None

        return new_start
