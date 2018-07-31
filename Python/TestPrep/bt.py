#!/usr/bin/python

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self,root, data):
        while self.data:
            if root == None:
                root = Node(data)
                break
            elif self .data <  data:
                if self.left == None:
                    self.left = Node(data)
                    break
                else:
                    self.left.insert(root, data)
            else:
                if self.right == None:
                    self.right = Node(data)
                    break
                else:
                    self.right.insert(root, data)
    def inOrder(self):
        if self != None:
            self.inOrder(self.left)
            print(self.data)
            self.inOrder(self.right)
    def preOrder(self):
        if self != None:
            print(self.data)
            self.preOrder(self.left)
            self.preOrder(self.right)
    def postOrder(self):
        if self != None:
            self.postOrder(self.left)
            self.postOrder(self.right)
            print(self.data)



root = Node(10)
