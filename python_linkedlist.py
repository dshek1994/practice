#!/usr/bin/env python3

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    
    #Print the linkedlist
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)

        #Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode
    
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        
        laste = self.headval

        while(laste.nextval):
            laste = laste.nextval

        laste.nextval = NewNode
    
    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    
    def RemoveNode(self, Removekey):
        HeadVal = self.headval

        if(HeadVal is not None):
            if(HeadVal.dataval == Removekey):
                self.head = HeadVal.nextval
                HeadVal = None
                return
        
        while(HeadVal is not None):
            if(HeadVal.dataval == Removekey):
                break

            prev = HeadVal
            HeadVal = HeadVal.nextval

            if(HeadVal == None):
                return
            
            prev.nextval = HeadVal.nextval

            HeadVal = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thur")

#Link first Node to second node
list1.headval.nextval = e2

#Link second node to the third node
e2.nextval = e3

#Link third node to the fourth node
e3.nextval = e4

list1.AtBeginning("Sun")
list1.AtEnd("Fri")
list1.AtEnd("Sat")

list1.Inbetween(list1.headval.nextval, "Sun")
list1.RemoveNode("Mon")

list1.listprint()

