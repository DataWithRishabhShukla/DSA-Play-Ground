# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        pass



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from queue import PriorityQueue

def mergeKLists( A):
    pq = PriorityQueue()

    for node in A :
        if node:
            pq.put((node.val,id(node),node))

    dummy = ListNode(0)
    current = dummy
    
    while not pq.empty():
        val , _ , node = pq.get()
        current.next = node
        current = current.next

        if node.next :
            pq.put((node.next.val, id(node.next), node.next))
        
        return dummy.next
    

