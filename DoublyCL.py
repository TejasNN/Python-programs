# Create Doubly circular linkedlist using python

# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Create a LinkedList class    
class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # Method to add a node at begin of LL
    def insertFirst(self,data) -> None:
        new_node = Node(data)
        if (self.head == None and self.tail == None):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.tail.next = self.head
        self.head.prev = self.tail
        self.count += 1

    # Method to add a node at the end of L
    def insertLast(self,data) -> None:
        new_node = Node(data)
        if (self.head == None and self.tail == None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.tail.next = self.head
        self.head.prev = self.tail
        self.count += 1

    # Method to remove first node of linked list
    def deleteFirst(self) -> None:
        if (self.count == 0):
            return
        elif (self.count == 1):
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self.count -= 1

    # Method to remove last node of linked list
    def deleteLast(self) -> None:
        if (self.count == 0):
            return
        elif (self.count == 1):
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        self.count -= 1

    # Method to add a node at any index
    def insertAtPos(self,data,pos) -> None:
        if (pos < 1 or pos > self.count+1):
            print("Invalid index")
            return
        
        if (pos == 1):
            self.insertFirst(data)
        elif (pos == self.count+1):
            self.insertLast(data)
        else:
            new_node = Node(data)
            temp_node = self.head
            for i in range(pos-2):
                temp_node = temp_node.next
                i += 1
            new_node.next = temp_node.next
            temp_node.next.prev = new_node
            new_node.prev = temp_node
            temp_node.next = new_node
        self.count += 1

    # Method to remove at given index
    def deleteAtPos(self,pos) -> None:
        if (pos < 1 or pos > self.count):
            print("Invalid index")
            return
        
        if (pos == 1):
            self.deleteFirst()
        elif (pos == self.count):
            self.deleteLast()
        else:
            temp_node = self.head
            for i in range(pos-2):
                temp_node = temp_node.next

            temp_node.next = temp_node.next.next
            temp_node.next.prev = temp_node
        self.count -= 1

    def display(self) -> None:
        current_node = self.head
        for i in range(self.count):
            print("<- {} -> ".format(current_node.data), end=" ")
            current_node = current_node.next
            i += 1

    def llcount(self):
        return self.count

#llist = DoublyLL()
#llist.insertFirst(111)
#llist.insertFirst(101)
#llist.insertFirst(51)
#llist.insertFirst(21)
#llist.insertFirst(11)

#llist.display() 
#print("\nThe linked list has : {} elements".format(llist.llcount()))

#llist.insertAtPos(55,3)
#llist.display() 
#print("\nThe linked list has : {} elements".format(llist.llcount()))

#llist.deleteAtPos(3)
#llist.display() 
#print("\nThe linked list has : {} elements".format(llist.llcount()))

#llist.deleteFirst()
#llist.display() 
#print("\nThe linked list has : {} elements".format(llist.llcount()))

#llist.deleteLast()
#llist.display() 
#print("\nThe linked list has : {} elements".format(llist.llcount()))

llist = DoublyLL()    
choice = 0
value = 0
position = 0
while(1):
    print("Linked list operations :")
    print("1. Insert node at first position")
    print("2. Insert node at last position")
    print("3. Insert node at given position")
    print("4. Delete node at first position")
    print("5. Delete node at last position")
    print("6. Delete node at given position")
    print("7. Display the linked list")
    print("8. Count the number of nodes in linked list")
    print("9. Exit")
    choice = int(input("Enter your choice:"))
    
    match choice:
        case 1:
            value = int(input("Enter a value to insert :"))
            llist.insertFirst(value)
            continue
        case 2:
            value = int(input("Enter a value to insert :"))
            llist.insertLast(value)
            continue
        case 3:
            value = int(input("Enter a value to insert :"))
            position = int(input("Enter a position :"))
            llist.insertAtPos(value,position)
            continue
        case 4:
            llist.deleteFirst()
            continue
        case 5:
            llist.deleteLast()
            continue
        case 6:
            position = int(input("Enter a position :"))
            llist.deleteAtPos(position)
            continue
        case 7:
            llist.display()
            continue
        case 8:
            print("Number of elements in linked list are : {}".format(llist.llcount()))
            continue
        case 9:
            break
        case default:
            print("Invalid option")
            continue