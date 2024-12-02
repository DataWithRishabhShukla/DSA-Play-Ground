import os 

os.system("clear")

print("Section  - Advance DSA 02")
print("Module   - DSA: Queues: Implementation & Problems")
print("Problem  - Implementing Queue using the stack !!\n")


print("IMP Points - Why copying is required in the peek ?? !!\n")
class UserQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []  # stack 1 
        self.s2 = []  # stack 2
        self.size = 0 # variable to track size 
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)
        self.size += 1
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.s2) == 0 :
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())


        if len(self.s2) > 0 :
            self.size -= 1
            return self.s2.pop()
            
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.s2) > 0  :
            return self.s2[-1]
        else :
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
            return self.s2[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.size == 0


import os 

os.system("clear")

print("Section  - Advance DSA 02")
print("Module   - DSA: Queues: Implementation & Problems")
print("Problem  - Implementing Dqeueue !!\n")

from collections import deque

def test_dequeue():
    dq = deque()

    dq.append(1)  # insert at the end 
    dq.append(2)
    dq.append(3)
    dq.append(4)
    print(dq)

    dq.appendleft(2)  # insert at the beginning  
    print(dq)

    print(dq.pop())  # delete from the end
    print(dq)

    print(dq.popleft())  # delete from the start 
    print(dq)



test_dequeue()


import os 

os.system("clear")

print("Section  - Advance DSA 02")
print("Module   - DSA: Queues: Implementation & Problems")
print("Problem  - Implementing sliding window maximum !!\n")

def sliding_window_maximum(arr,B):
    n = len(arr)
    dq = deque()
    ans = []

    for i in range(B):

        while len(dq) >0 and arr[i] >= arr[dq[-1]]:
            dq.pop()

        dq.append(i)

    for i in ans :
        print(arr[i], end= " ")

    ans.append(dq[0])

    start = 1

    for i in range(B,n):
        while len(dq) > 0 and arr[i] >= arr[dq[-1]]:
            dq.pop()
        
        dq.append(i)

        if len(dq) > 0 and dq[0] < start :
            dq.popleft()
        
        
        start += 1
        ans.append(dq[0])
    
    for i in ans :
        print(arr[i], end= " ")
   
        

A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3

A = [10,9,8,7,6,5,4,3,2,1]
B = 2
sliding_window_maximum(A,B)