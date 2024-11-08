
def start_new(func_name):
    import os 
    os.system("clear")
    print(f"Proessing for : {func_name}!!!\n")


def find_using_binary_search(arr,k):
    l , r = 0 , len(arr)-1

    while l <= r :
        mid = (l+r) // 2

        if arr[mid] == k:
            print(f"Element {k} found at {mid}th position !!!")
            return
        
        elif arr[mid] > k:
            r = mid - 1
        else :
            l = mid + 1

    print(f"Element {k} not found in the array !!!") 

start_new("Binary Search !!")


A = [1,2,3,4,6,7,8,9]
find_using_binary_search(A,6)


def find_first_mail(arr,k):

    l , r = 0 , len(arr) - 1
    ans = -1 

    while l <= r:
        mid = (l+r) //2 

        if arr[mid] == k:
            ans = mid 
            r = mid - 1
        elif arr[mid] > k :
            r = mid - 1
        else :
            l = mid + 1
    
    print(f"First occurance of {k} is found at position {ans}")



start_new("Q1. Search for a Range !!")
A = [5, 7, 7, 8, 8, 10]
B = 5
find_first_mail(A,B)

A = [5,5, 7, 7, 8, 8, 10]
ans = 0
for ele in A :
    ans = ans ^ ele

print(ans)