# Define the Node class
class Node:
    def __init__(self, data):
        # Initialize a node with data and a next pointer
        self.data = data
        self.next = None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with a head pointer
        self.head = None

    def append(self, data):
        # Append a new node with data at the end of the linked list

        # Create a new node
        new_node = Node(data)

        # If the linked list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the end of the linked list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # Set the next pointer of the last node to the new node
        last_node.next = new_node

    def print_list(self):
        # Print the elements of the linked list

        # Initialize a pointer to the head of the linked list
        current_node = self.head

        # Traverse and print each node's data
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Create a linked list object
my_list = LinkedList()

# Append elements to the linked list
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

# Print the linked list
my_list.print_list()
