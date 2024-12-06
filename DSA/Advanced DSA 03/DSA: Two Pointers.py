import os 

os.system("clear")

print("Section  - Advance DSA 03")
print("Module   - DSA: Two Pointers")
print("Problem  - Pair with given sum k !!\n")


def find_pair(arr,st,end,k):

    while st <= end:

        mid = (st + end ) // 2

        if arr[mid] == k :
            print(f"Pair k found at {mid} with value {k}")
            return True
        elif arr[mid] > k :
            end = mid - 1
        else :
            st = mid + 1
    
    return False

arr = [3,7,8,11,14,19,25]
n = len(arr)
k = 26
for idx in range(n):

    if find_pair(arr,idx+1,n-1,k-arr[idx]) :
        print(f"First element of the pair is :{arr[idx]}")

