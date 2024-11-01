def start_new(func_name):
    import os 
    os.system("clear")
    print(f"Solving for : {func_name}!!!\n")


from functools import cmp_to_key

def cmp_custom(x,y):
    if x + y > y + x:
        return -1
    elif x == y :
        return 0
    else :
        return 1
    
start_new("Q1. Largest Number")

arr = [3, 30, 34, 5, 9]
nums = [str(num) for num in arr]
print(nums)

nums.sort(key= cmp_to_key(cmp_custom))

print(nums)
print(f"\n String representaion is : {''.join(nums)}")


def count_factors(x):
    count = 0
    i = 1
    while i*i <= x:
        if x %i == 0:
            if x /i == i: 
                count += 1
            else :
                count += 2
        i += 1
    
    #print(f"number of count for {x} are {count} !!")
    return count

def cmp_custom_facotrs(x,y):
    if count_factors(x) == count_factors(y):
        if x < y :
            return -1 
        elif x == y :
            return 0
        else :
            return 1
    elif count_factors(x) < count_factors(y):
        return -1
    else :
        return 1

start_new("Q3. Factors sort !!")
count_factors(9)

A = [6, 8, 9]
print(f"Array before sorting : {A}")
A.sort(key = cmp_to_key(cmp_custom_facotrs))
print(f"Array after sorting : {A}")



def partition_pivot(arr):
    n = len(arr)
    l , r = 0 , n-2
    pivot = arr[n-1]
    print(f"Initial Array :{arr}")
    while l <=r :
        if arr[l] < pivot :
            l += 1
        elif arr[r] > pivot :
            r -= 1
        else :
            arr[l],arr[r] = arr[r] , arr[l]
    
    print(f"Value at l {l} index :{arr[l]}")
    print(f"Value at r {r} index :{arr[r]}")
    print(f"Array after fixing the order : {arr}")
    print("Swapping the pivot element with l index !!")
    arr[n-1] , arr[l] = arr[l] , arr[n-1]
    print(f"Final array pivoting :{arr}")
    


start_new("Q5. Partition Index !!")
A = [6, 2, 0, 4, 5]
partition_pivot(A)



def sort_by_color(A):

    n = len(A)
    i = 0
    st_pnt = 0
    end_pnt = n-1

    while i <= end_pnt :

        if A[i] == 0:
             A[i] , A[st_pnt] = A[st_pnt] ,A[i]
             i += 1
             st_pnt += 1
        elif A[i] == 2:
             A[i] , A[end_pnt] = A[end_pnt] ,A[i]
             end_pnt -= 1
        else :
            i += 1
    
    
    print(f"Array after sorting is : {A}")


start_new("Q2. Sort by Color !!")
A = [0, 1, 2, 0, 1, 2]
# A =[0]
sort_by_color(A)

