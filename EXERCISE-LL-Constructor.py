class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
    ## WRITE LL CONSTRUCTOR HERE ##
    #                             #
    #                             #
    #                             #
    #                             #
    ###############################


my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""
