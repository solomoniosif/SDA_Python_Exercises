##########################################
# TODO: Single Linked List Implementation
##########################################


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            nodes = list(nodes)
            node = Node(value=nodes.pop(0))
            self.head = node
            for next_node in nodes:
                node.next = Node(value=next_node)
                node = node.next

    def tail(self):
        if self.head is None:
            return None
        current = self.head
        while True:
            if current.next is None:
                return current
            current = current.next

    def add_first(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_el = self.tail()
        last_el.next = new_node

    def add_after(self, target_node_value, value):
        new_node = Node(value)
        if self.head is None:
            raise Exception('List is empty!')
        for node in self:
            if node.value == target_node_value:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception(f'Node with value {target_node_value} not found!')

    def add_before(self, target_node_value, value):
        new_node = Node(value)
        if self.head is None:
            raise Exception('List is empty!')
        if self.head.value == target_node_value:
            return self.add_first(value)
        prev_node = self.head
        for node in self:
            if node.value == target_node_value:
                new_node.next = node
                prev_node.next = new_node
                return
            prev_node = node
        raise Exception(f'Node with value {target_node_value} not found!')

    def add_nodes(self, nodes):  # Method for adding multiple nodes at the end of the list
        nodes = list(nodes)
        if self.head is None:
            self.head = Node(value=nodes.pop(0))
            prev_node = self.head
        prev_node = self.tail()
        for node_value in nodes:
            new_node = Node(value=node_value)
            prev_node.next = new_node
            prev_node = new_node

    def remove_node(self, target_node_value):
        if self.head is None:
            raise Exception(f'List is empty!')
        if self.head.value == target_node_value:
            self.head = self.head.next
            return
        prev_node = self.head
        for node in self:
            if node.value == target_node_value:
                prev_node.next = node.next
                return
        raise Exception(f'Node with value {target_node_value} not found!')

    def reverse(self):
        if self.head is None:
            return self
        if self.head.next is None:
            return self.head
        reversed_ll = LinkedList()
        for node in self:
            reversed_ll.add_first(node.value)
        return reversed_ll

    def get(self, index):
        if index > len(self) - 1:
            raise IndexError('list index out of range')
        for i, node in enumerate(self):
            if i == index:
                return node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        if self.head is None:
            return 0
        current = self.head
        elements = 1
        while True:
            if current.next is None:
                return elements
            current = current.next
            elements += 1

    def __repr__(self):
        if self.head is None:
            return 'Empty LinkedList'
        ll_repr = []
        for node in self:
            ll_repr.append(f"[{node.value} -> ({node.next})]")
        return ', '.join(ll_repr)


if __name__ == '__main__':
    # Initialization of an empty linkedlist
    llist = LinkedList()
    print(f"\nThe list initialized with no nodes: \n  -->  {llist}")

    # Adding multiple nodes at the end of the list
    llist.add_nodes('ijklm')
    print(f"\nThe list after adding multiple nodes at once at the end of the list: \n --> {llist}")

    # Adding a node at the beginning
    llist.add_first('b')
    print(f"\nThe list after adding 'b' at the beginning: \n  -->  {llist}")
    llist.add_first('a')
    print(f"\nThe same list after adding 'a' at the beginning: \n  -->  {llist}")

    # A new linkedlist initialized with nodes
    llist2 = LinkedList(["a", "b", "c", "d", "e"])
    print(f"\nA new linkedlist initialized with nodes: \n  -->  {llist2}")

    # Getting the length of the list
    print(f"\nThe length of the list:  \n  -->  {len(llist2)}")

    # Adding a node at the end
    llist2.add_last('z')
    print(f"\nThe list after adding 'z' at the end: \n  -->  {llist2}")

    # Getting the tail of the list
    print(f"\nThe tail of the list: \n  -->  {llist2.tail()}")

    # Adding 'f' after 'e'
    llist2.add_after('e', 'f')
    print(f"\nThe list after adding 'f' after 'e': \n  -->  {llist2}")

    # Adding 'y' before 'z'
    llist2.add_before('z', 'y')
    print(f"\nThe list after adding 'y' before 'z': \n  -->  {llist2}")

    # Getting the node at a given index
    print(f"\nThe node at index 3: \n --> {llist2.get(3)}")

    # Removing the node 'b'
    llist2.remove_node('b')
    print(f"\nThe list after removing the node 'b': \n  -->  {llist2}")

    # Reversing the list (current implementation returns a new reversed list)
    reversed_llist2 = llist2.reverse()
    print(f"\nThe reversed list:\n  -->  {reversed_llist2}")