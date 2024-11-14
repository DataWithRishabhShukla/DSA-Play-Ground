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