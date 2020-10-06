# Define node class of Linked List
class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    # Print the Linked List from the beginning to the end.
    def print(self):
        print("Count: ", self.count, ' / ', end=' ')
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()
    
    # Add a new node at the end of the current Linked List
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
        self.count += 1
    
    # Return the index of a node with
    # input data of its first appearance.
    # If the Linked List has no such data, return -1.
    def getIndex(self, data):
        cur = self.head
        idx = 0
        while cur:
            if cur.data == data: return idx
            cur = cur.next
            idx += 1
        return -1
    
    # Return the data of a node with a given index.
    # If index is out of range, print error message
    # and return None.
    def getData(self, idx):
        if idx > self.count:
            print("Index out of range")
            return None
        cur = self.head
        ptr = 0
        while ptr != idx:
            ptr += 1
            cur = cur.next
        return cur.data
    
    # Insert a node at the given index.
    def insertNodeAtIndex(self, idx, node):
        # Insert a node at the beginning of the Linked List.
        if idx == 0:
            node.next = self.head
            self.head = node
            self.count += 1
        
        # Insert a node at the end of the Linked List.
        elif idx == self.count:
            self.append(node)
        
        # Insert a node in the middle of the Linked List.
        else:
            cur = self.head
            ptr = 0
            while ptr < idx - 1:
                ptr += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node
            self.count += 1
        
    # Insert a node at a given data.
    def insertNodeAtData(self, data, node):
        idx = self.getIndex(data)
        # If no such data exists
        if idx == -1:
            print("No such data exists")
        else:
            self.insertNodeAtIndex(idx, node)
    
    # Delete the node at the given index.
    def deleteIndex(self, idx):
        cur = self.head
        # If deleting the tail
        if idx == -1:
            idx = self.count - 1
        # If deleting the head
        if idx == 0:
            self.head = self.head.next
            # delete cur
        # If index is out of range
        if idx >= self.count:
            print("Index out of range")
        else:
            ptr = 0
            while ptr < idx - 1:
                ptr += 1
                cur = cur.next
            target = cur.next
            cur.next = target.next
            # delete target
        
        self.count -= 1
    
    # Empty Linked List
    def clear():
        # Delete from the tail
        self.head = None

if __name__ == '__main__':
    LL1 = LinkedList()
    LL1.append(LLNode(3))
    LL1.append(LLNode(6))
    LL1.append(LLNode(2))
    LL1.print()
    print()
    
    print("Index of data 2: ", LL1.getIndex(2))
    print()
    
    LL1.insertNodeAtIndex(2, LLNode(7))
    LL1.print()
    LL1.insertNodeAtIndex(0, LLNode(4))
    LL1.print()
    LL1.insertNodeAtIndex(5, LLNode(8))
    LL1.print()
    print()
    
    LL1.insertNodeAtData(6, LLNode(10))
    LL1.print()
    LL1.insertNodeAtData(100, LLNode(13))
    print()
    
    LL1.deleteIndex(3)
    LL1.print()
    LL1.deleteIndex(0)
    LL1.print()
    LL1.deleteIndex(4)
    LL1.print()
    LL1.deleteIndex(4)
    print()