
import os 

os.system("clear")

print("Section   - Advance DSA 02")
print("Module    - DSA: Searching 3: Binary Search on Answer")
print("Problem 1 - Painter's Problem !!\n")


def count_no_painters(arr,t):
    ans = 1 
    curr_cap = 0

    for i in range(len(arr)):
        if arr[i] > t :
            print("Job can not be completed in t Time !!!")
            return
        if arr[i] + curr_cap <= t :
            curr_cap += arr[i]
        else :
            ans+=1
            curr_cap = arr[i]
    
    print(f"Number of painter required are : {ans}")

def is_possible(arr, t, p):
    """
    This has number of the painters and time in hand .
    We have to check if job can be completed in the given numbers of painters. 
    """

    cnt = 1
    curr = 0

    for i in range(len(arr)):
        if arr[i] > t :
            print("Job can not be completed !!!")
            return

        if curr + arr[i] <= t :
            curr += arr[i]
        else :
            cnt += 1
            curr = arr[i]

    
    return True if cnt <= p else False


def find_min_time(arr,p):
    """
    We have fixed number of painters we have to find the minimum number of time required for finishing the project.
    There is no direct way to distribute the work so will use the binary search to find the solution .
    we require three things for it 
        serach space 
        condition 
        target
    """

    l = max(arr) # this is the minimum time requred to finish one task
    r = sum(arr) # This is the maximum time , in this time one person can finish the job 

    ans = float("-inf")
    while l <=r :
        mid = (l+r) // 2

        status = is_possible(arr,mid,p)
        if status :
            ans = mid
            r = mid -1
        else :
            l = l+1
    
    print(f"Minimum time required to finish the job is :{ans}")
    print((ans * 10) %10000003)

A =[10,20,30,40]
T = 50
#count_no_painters(A,T)
# print(is_possible(A,T,3))

# find_min_time(A,3)


A = [884,228,442,889]
find_min_time(A,4)

#################################################################################

import os 

os.system("clear")

print("Section   - Advance DSA 02")
print("Module    - DSA: Searching 3: Binary Search on Answer")
print("Problem 1 - Aggresive cows Problem !!\n")


def place_cows(arr, dist, no_of_cows):

    cnt = 1
    las_pos =arr[0]

    for i in range(1,len(arr)):

        if las_pos + dist <= arr[i]:
            cnt += 1
            las_pos = arr[i]

        if cnt == no_of_cows :
            return True
    
    return False

def aggresive_cows(arr,b):
    n = len(arr)
    l = 0
    r = arr[n-1] - arr[0]
    ans = float("inf")

    while l <= r:

        mid = (l+r) // 2 

        status = place_cows(arr,mid,b)
        if status :
            ans = mid
            l = mid + 1
        else :
            r = mid - 1

    return ans 




A = [1, 2, 3, 4, 5]
B = 3

print(aggresive_cows(A,B))
