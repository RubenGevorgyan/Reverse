class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class Reverse:
    def __init__(self):
        self.headval = None

    def addnode(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval=NewNode

    def printlist(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def appendAfter(self, previous_node, new_data):
        if previous_node is None:
            print "The given previousious node must in LinkedList."
            return
        new_node = winner(new_data)
        new_node.nextval = previous_node.nextval
        previous_node.nextval = new_node

    def deleteNode(self, position):
        if self.headval == None:
            return
        temp = self.headval
        if position == 0:
            self.headval = temp.nextval
            temp = None
            return
        for i in range(position - 1):
            temp = temp.nextval
            if temp is None:
                break
        if temp is None:
            return
        if temp.nextval is None:
            return
        nextval = temp.nextval.nextval
        temp.nextval = None
        temp.nextval = nextval

    def reverse(self):
        previous = None
        current = self.headval
        while (current is not None):
            nextval = current.nextval
            current.nextval = previous
            previous = current
            current = nextval
        self.headval = previous

    def find(self, data):
        temp = self.headval
        while temp.nextval.data is not data:
            temp = temp.nextval


def main ():
    rev=Reverse()
    for i in range(0,int(raw_input("How many inputs do you want to input? \n"))):
        rev.addnode(raw_input())
    rev.reverse()
    rev.printlist()
main()
