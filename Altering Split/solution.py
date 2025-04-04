class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    flag = True  
    result = Context(head, head.next)  
    
    temp1 = result.first  
    temp2 = result.second  
    current = head.next  

    while current.next is not None:  
        if flag:  
            temp1.next = current.next  
            temp1 = temp1.next  
            current = current.next  
            flag = False  
        else:  
            temp2.next = current.next  
            temp2 = temp2.next  
            current = current.next  
            flag = True  
    else:  
        temp1.next = None  
        temp2.next = None  

    return result  
