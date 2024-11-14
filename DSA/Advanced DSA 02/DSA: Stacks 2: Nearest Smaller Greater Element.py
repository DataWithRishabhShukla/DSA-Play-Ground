import os 

os.system("clear")

print("Section   - Advance DSA 02")
print("Module    - DSA: Stacks 2: Nearest Smaller/Greater Element")
print("Problem 1 -  Nearest smaller on the Left side !!\n")

def nearest_smaller_on_left(arr):
    n = len(arr)
    ans = [-1] * n
    stk = []
    for i in range(n):
        while len(stk) > 0 and stk[-1] >= arr[i] :
            stk.pop()

        if len(stk) > 0:
            ans[i] = stk[-1]
        
        stk.append(arr[i])
    
    print(f"arr is :{arr}")
    print(f"ans is :{ans}")


A = [5,2,8,10,6,1,7,15]
A = [4,5,2,10,3,2]
nearest_smaller_on_left(A)


os.system("clear")

print("Section   - Advance DSA 02")
print("Module    - DSA: Stacks 2: Nearest Smaller/Greater Element")
print("Problem 1 -  Nearest smaller on the Left side - return index !!\n")

def nearest_smaller_on_left_index(arr):
    n = len(arr)
    ans = [-1] * n
    stk = []
    for i in range(n):
        while len(stk) > 0 and arr[stk[-1]] >= arr[i] :
            stk.pop()

        if len(stk) > 0:
            ans[i] = stk[-1]
        
        stk.append(i)
    
    print(f"arr is :{arr}")
    print(f"ans is :{ans}")

A = [4,5,2,10,3,2]
nearest_smaller_on_left_index(A)

os.system("clear")
print("Section   - Advance DSA 02")
print("Module    - DSA: Stacks 2: Nearest Smaller/Greater Element")
print("Problem 1 -  Nearest greater on the Left side  !!\n")

def nearest_greater_on_left(arr):
    n = len(arr)
    ans = [-1] * n
    stk = []
    for i in range(n):
        while len(stk) > 0 and  arr[i] >= stk[-1] :
            stk.pop()

        if len(stk) > 0:
            ans[i] = stk[-1]
        
        stk.append(arr[i])
    
    print(f"arr is :{arr}")
    print(f"ans is :{ans}")

A = [4,5,2,10,3,2]
nearest_greater_on_left(A)



os.system("clear")
print("Section   - Advance DSA 02")
print("Module    - DSA: Stacks 2: Nearest Smaller/Greater Element")
print("Problem 1 -  Nearest greater on the right side  !!\n")


def nearest_greater_on_right(arr):
    n = len(arr)
    stk =[]
    ans = [-1] * n

    for i in range(n-1,-1,-1):
        while len(stk) > 0 and arr[i] >= stk[-1]:
           stk.pop()
        
        if len(stk) > 0:
           ans[i] = stk[-1]

        stk.append(arr[i])
    
    print(f"arr is :{arr}")
    print(f"ans is :{ans}")


arr = [7,9,3,5,8,11,6]
nearest_greater_on_right(arr)


os.system("clear")
print("Section   - Advance DSA 02")
print("Module    - DSA: Stacks 2: Nearest Smaller/Greater Element")
print("Problem 4 - Largest Rectangle in Histogram  !!\n")

def largestRectangleArea(A):
    # find the nearest smaller on the left 
    # find the nearest smaller on the right

    n = len(A)
    left = [-1]*n
    stk = []

    print(f"Original array is     : {A}")
    for i in range(n):
        while len(stk) > 0 and A[i] <= A[stk[-1]]:
            stk.pop()
        
        if len(stk) > 0:
            left[i] = stk[-1]
        stk.append(i)
    
    print(f"Smallest on the left  : {left}")

    right = [-1] * n 
    stk = []

    for i in range(n-1,-1,-1):
        while len(stk) > 0 and A[i] <=  A[stk[-1]]:
            stk.pop()
        
        if len(stk) > 0:
            right[i] = stk[-1]
        stk.append(i)

    print(f"Smallest on the right : {right}")
    
    for i in range(n):
        if right[i] == -1 :
            right[i] = n
    
    print(f"Smallest on the right : {right}")
    
    ans = float("-inf")
    for i in range(n):
        h = A[i]
        x1 = left[i]
        x2 = right[i]
        w = x2 - x1 - 1
        area = h * w
        ans = max(ans,area)
    
    print(f"Max area by recatugular is :{ans}")



A = [2, 1, 5, 6, 2, 3]
largestRectangleArea(A)

