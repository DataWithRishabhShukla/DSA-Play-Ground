
def give_nom_of_bit(num):
    print(f"decimal rep :{num}")
    count = 0
    while num > 0:
        if num & 1 > 0:
            count +=1
        
        num = num >> 1
    
    return count


# print(give_nom_of_bit(11))


def solve(A):
    cnt = 0
    while A > 0:
        if (A & 1) > 0:
            cnt += 1
            A = A - 1 
        else :
            A = A >> 1
    
    print(f"Number of times help taken  :{cnt}")


solve(7)


def max_sum_sub_array(arr):
    max_sum = 0

    for i in range(len(arr)):
        sum1 = 0
        for j in range(i,len(arr)):
            sum1 += arr[j]
            max_sum = max(max_sum,sum1)
    
    print(f"max_sum is {max_sum}")

# max_sum_sub_array([1,2,3])

# max_sum_sub_array([-3,2,4,-1,3,-4,3])


def start_new(func_name):
    import os 
    os.system("clear")
    print(f"Proessing for : {func_name}")

def first_non_repaeating_ele(arr):
    freq  = {}
    for num in arr :
        if num in freq :
            freq[num] += 1
        else :
            freq[num] = 1
    
    for num in arr :
        if freq[num] == 1:
            return num 
    
    return -1 

arr = [4,3,3,2,5,6,4,5]
start_new("first_non_repaeating_ele")
print(first_non_repaeating_ele(arr) )


def print_all_subarry(arr):
    n = len(arr)
    for si in range(n):
        for ei in range(si,n):
            #print(f"value os si ei : {si,ei}")
            for k in range(si,ei+1):
                print(arr[k])
            
            print()



def solve(arr,B):

    count = 0 
    hs = {}
    for num in arr :

        right_pair = num - B
        left_pair = num + B
        if  right_pair in hs :
            count = count + hs[right_pair]
        
        if  left_pair in hs :
            count = count + hs[left_pair]
        
        if num in hs :
            hs[num] += 1
        else :
            hs[num] = 1

    return count 


start_new("a[i] - a[j] = B")
arr = [1, 2, 1, 2]
B = 1
print(solve(arr, B))


start_new("printing_all_subarray")
arr = [1,2,3]
print_all_subarry(arr)



def subarray_with_sum_b(A,B):
    n = len(A)
    psum = [0] * n
    psum[0] = A[0]
    print(psum)
    for i in range(1,n):
        psum[i] = psum[i-1] + A[i]

    print(psum)
    cnt = 0
    hm = {}
    for num in psum:
        if num == B :
            cnt += 1  
        
        if num - B in hm :
            cnt += hm[num-B]

        if num in hm :
            hm[num] += 1
        else :
            hm[num] = 1
    
    print( cnt)
 
start_new("printing_all_subarray_withsum_B")
A = [1, 0, 1]
B = 1

A = [0, 0, 0]
B = 0
subarray_with_sum_b(A,B)


start_new("Longest Subarray Zero SumB")
A = [1, 0, 1]
B = 1

A = [0, 0, 0]
B = 0
subarray_with_sum_b(A,B)