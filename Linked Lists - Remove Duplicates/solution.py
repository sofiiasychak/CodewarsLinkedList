def remove_duplicates(head):
    """
    Solution of the task.
    """
    if head is None:
        return None

    current_node = head

    while current_node != None:
        if current_node.next != None:
            if current_node.data == current_node.next.data:
                next_next_node = current_node.next.next
                current_node.next = next_next_node
            else:
                current_node = current_node.next
        else:
            current_node = current_node.next

    return head
