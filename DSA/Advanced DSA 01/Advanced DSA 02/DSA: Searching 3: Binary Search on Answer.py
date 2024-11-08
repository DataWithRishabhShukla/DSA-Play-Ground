
import os 

os.system("clear")

print("Section   - Advance DSA 02")
print("Module    - DSA: Searching 3: Binary Search on Answer")
print("Problem 1 - Aggrresive Cows Problem !!\n")


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


A =[10,20,30,40]
T = 30
count_no_painters(A,T)