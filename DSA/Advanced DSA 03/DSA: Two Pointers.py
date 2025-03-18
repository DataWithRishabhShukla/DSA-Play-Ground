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



import os 

os.system("clear")

print("Section  - Advance DSA 03")
print("Module   - DSA: Two Pointers")
print("Problem  - Pair with given sum k using the 2 pointer approach !!\n")



def sum_pair_using_two_p(arr,k):
    n = len(arr)
    l , r = 0 , n - 1

    while l < r :
        sum = arr[l] + arr[r]

        if sum == k :
            print(f"sum {k} is possible with : {arr[l] , arr[r]}")
            return
        elif sum > k :
            r -= 1
        else :
            l += 1
    
    print(f"Sum is not possible !!!")

arr = [-3,7,8,11,14,19,25]

k = 28

sum_pair_using_two_p(arr, k)


def count_sum_pair_using_two_p(arr,k):
    n = len(arr)
    l , r = 0 , n - 1
    count = 0
    while l < r :
        sum = arr[l] + arr[r]

        if sum == k :
            print(f"sum {k} is possible with : {arr[l] , arr[r]}")
            count += 1
            l += 1
            r -= 1
        elif sum > k :
            r -= 1
        else :
            l += 1
    
    print(f"Number of pairs possible are : {count} !!!")

arr = [-3,7,8,11,14,19,25]

k = 27

count_sum_pair_using_two_p(arr, k)


os.system("clear")

print("Section  - Advance DSA 03")
print("Module   - DSA: Two Pointers")
print("Problem  - Pair with given sum k using the 2 pointer approach - duplicates!!\n")


# arr = [2,3,3,3,10,10,10,15]
def count_pair_sum_with_duplicates(arr,k):

    l , r = 0 , len(arr)-1
    count = 0

    while l < r :
        sum = arr[l] + arr[r]

        if sum == k:
            if arr[l] == arr[r]:
                c1 = r - l + 1
                temp = int((c1-1) * c1 /2)
                count += temp
                break

            c1 , c2 = 1 , 1 

            while l < r and arr[l] == arr[l+1]:
                print(f"Current Value of l is :{l} ")
                c1 += 1
                l += 1
            
            while l < r and arr[r] == arr[r-1]:
                c2 += 1
                r -= 1

            print(f"Value of c1,c2 is : {c1,c2}")
            count += (c1 * c2)
            l += 1
            r -= 1
 
        elif sum > k :
            r -= 1
        else :
            l += 1
    
    print(f"Total number of pair with sum {k} are : {count}")

arr = [2,3,3,3,10,10,10,15]
arr =[5,5,5,5,5,5]
count_pair_sum_with_duplicates(arr,10)


os.system("clear")

print("Section  - Advance DSA 03")
print("Module   - DSA: Two Pointers")
print("Problem  - Pair with difference !!\n")

def pair_with_diff_k(arr,k):
    
    l , r = 0 , 1

    while l < r :
        diff = arr[r] - arr[l]
        if diff == k:
            print(f"Diff with {k} exist with pair {arr[l],arr[r]}")
            return True
        elif diff > k :
            l += 1
        else :
            r += 1
    
    return False 


arr = [-3,0,1,3,6,8,11,14,21,25]
pair_with_diff_k(arr,5)


os.system("clear")

print("Section  - Advance DSA 03")
print("Module   - DSA: Two Pointers")
print("Problem  - Count Pair with difference !!\n")

def count_pair_with_diff_k(arr,k):
        n = len(arr)
        arr.sort()

        count = 0 
        i , j = 0 , 1 

        while j < n :
            if j == i :
                j += 1 
                continue
        
            x , y = arr[i] , arr[j]

            if y - x == k :
                count += 1
                while i < n and arr[i] == x :
                    i += 1
                
                while j < n and arr[j] == y :
                    j += 1

            elif y - x > k :
                i += 1
            else :
                j += 1
            
        print(f"Total possible pairs are :{count}")

        
arr = [8,5,1,10,5,9,9,3,5,6,6,2,8,2,2,6,3,8,7,2,5,3,4,3,3,2,7,9,6,8,7,2,9,10,3,8,10,6,5,4,2,3]
arr = [8, 12, 16, 4, 0, 20]
k = 4 

count_pair_with_diff_k(arr,k)
