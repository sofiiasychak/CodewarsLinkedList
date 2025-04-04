def swap_pairs(head):
    """
    Solution of the task.
    """
    if not head or not head.next:
        return head

    current_node = head
    list_of_nodes = []
    while current_node:
        list_of_nodes.append(current_node)
        current_node = current_node.next

    if len(list_of_nodes) % 2 == 0:
        for i in range(0, len(list_of_nodes), 2):
            current_node = list_of_nodes[i]
            next_node = list_of_nodes[i + 1]
            list_of_nodes[i] = next_node
            list_of_nodes[i + 1] = current_node
    else:
        for i in range(0, len(list_of_nodes) - 1, 2):
            current_node = list_of_nodes[i]
            next_node = list_of_nodes[i + 1]
            list_of_nodes[i] = next_node
            list_of_nodes[i + 1] = current_node

    for i in range(len(list_of_nodes) - 1):
        list_of_nodes[i].next = list_of_nodes[i + 1]
    list_of_nodes[-1].next = None

    return list_of_nodes[0]
