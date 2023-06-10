class Node:
    def __init__(self,data):
        self.data=2
        self.link=None


class LinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None

    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        self.lastNode =self.head
        while self.lastNode.link:
            self.lastNode = self.lastNode.link
        
        self.lastNode.link = newNode

    def prepend(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        newNode.link = self.head
        self.head = newNode

    def showlist(self):
        currNode = self.head
        while currNode:
            print(currNode.data, end="->")
            currNode = currNode.link
        print("None")


# menghapus elemen diawal
    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete") 
            return
        self.start_node = self.start_node.ref

list = LinkedList()
list.append(3)
list.prepend(4)
list.prepend(5)
list.showlist(0)


