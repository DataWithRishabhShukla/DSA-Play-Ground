import os 

os.system("clear")

print("Section   - Advance DSA 02")
print("Module    - DSA: Classes, Objects & Linked List Introduction ")
print("Problem 1 - Creating - Traversing a Linked List !!\n")

class Node :
    def __init__(self,x):
        self.data = x
        self.next = None


def traverse(head):
    """ Function to traverse  a linked List !!"""
    tmp = head

    while tmp != None:
        print(tmp.data , end = " ")
        tmp = tmp.next 
    print()

a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c

traverse(a)



