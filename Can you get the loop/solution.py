def loop_size(node):
    """
    Solution for the problem.
    """
    steps = 1  
    visited = {node: steps}

    while True:
        node = node.next  
        steps += 1  

        if node in visited:  
            return steps - visited[node]  

        visited[node] = steps  
