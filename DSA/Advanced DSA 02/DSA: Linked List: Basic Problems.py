
import os 

os.system("clear")

print("Section   - Advance DSA 02")
print("Module    - DSA: Linked List: Basic Problems")
print("Problem 1 - Check if x is present in LL !!\n")

class Node :
    def __init__(self,x):
        self.data = x
        self.next = None


def find_x(head, x):
    tmp = head
    while tmp != None :
        if tmp.data == x :
            print(f"Element : {tmp.data} Found !!")
            return

        tmp = tmp.next
    print(f"Element : {x} not found in the LL !!")
    return -1
    
def insert_x_pos(head,pos,data):
    pass

def delte_first_x(head, pos):
    pass

a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c

find_x(a, 200)



import os 

os.system("clear")

print("Section   - Advance DSA 02")
print("Module    - DSA: Linked List: Basic Problems")
print("Problem 4 - Deep Copy LL without using the extra space !!\n")

class Node :
    def __init__(self,x):
        self.data = x
        self.next = None
        self.random  = None

def print_list(head):
    tmp = head

    while tmp != None :
        print(tmp.data , end = " ")
        
        # print( tmp.next.data , tmp.random.data )
        tmp = tmp.next
    
    print("\n")

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b
b.next = c
c.next = d

a.random = c
b.random = a
c.random = d
d.random = b


print_list(a)

def deep_copy(head):
    curr = head 
    copied_head = head

    while  curr != None:

        nn = Node(curr.data)
        nn.next = curr.next 
        curr.next = nn 
        curr = curr.next.next 
    print("list after copying the  List !! ")
    print_list(head)

    curr = head 
    curr_1 = head.next 

    while curr != None :
        curr_1.random = curr.random.next 
        curr = curr.next.next 
        if curr != None :
            curr_1 =  curr_1.next.next
    
    print("list after updatng the  random !! ")
    print_list(head)

    curr = head 
    curr_1 = head.next 
    new_head  =  head.next 

    while curr != None :
        curr.next = curr_1.next 
        if curr.next != None :
            curr_1.next = curr_1.next.next 
        
        curr = curr.next 
        curr_1 = curr_1.next
    
    print("list after Delinking the List-1 !! ")
    print_list(head)

    print("list after Delinking the List-1 !! ")
    print_list(new_head)

deep_copy(a)