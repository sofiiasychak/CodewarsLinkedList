class Context(object):
    """
    Given class.
    """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    Solution of the task.
    """
    if source is None:
        raise IndexError

    new_node = source
    source = source.next

    new_node.next = dest
    dest = new_node

    return Context(source, dest)
