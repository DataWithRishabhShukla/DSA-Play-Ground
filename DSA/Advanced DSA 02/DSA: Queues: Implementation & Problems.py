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
