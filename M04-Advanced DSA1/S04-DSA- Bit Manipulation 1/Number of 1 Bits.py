
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



def longest_subsrray_withsum_zero(A):
    n = len(A)

    psum = [0] * n
    psum[0] = A[0]

    for i in range(1,n):
        psum[i] = psum[i-1] + A[i]
    
    print(A)
    print(psum)
    ans = 0
    hm = {}
    for j in range(n) :
        print(hm)
        if psum[j] == 0:
            ans = max(ans,j+1)
        
        if psum[j] in hm :
            print("Inside the if psum[j] exist ")
            print(f"Pre ans , j :{ans, j}")
            ans = max(ans,j- hm[psum[j]] )
            print(f"post ans , j :{ans, j}")
        else :
            hm[psum[j]] = j
    print(f"Maximum length is : {ans}")



start_new("Longest Subarray Zero Sum")

A = [1, -2, 1, 2]
A = [3, 2, -1]
A = [1, -2, 1, 2]
A = [9,-20,-11,-8,-4,2,-12,14,1]
A = [-16,16,1]
longest_subsrray_withsum_zero(A)



def distinct_number_in_window(A,B):
    hm = {}
    res = []

    for i in range(B):
        if A[i] in hm :
            hm[A[i]]    += 1
        else :
            hm[A[i]]    = 1 

    res.append(len(hm))

    for j in range(B,len(A)):
        out_ele = A[j-B]
        if hm[out_ele] == 1 :
            del hm[out_ele]
        else :
            hm[out_ele] -= 1
        
        in_ele = A[j]
        if in_ele in hm :
            hm[in_ele]    += 1           
        else :
            hm[in_ele]    = 1
        
        res.append(len(hm))
    
    print(res)

     

start_new("Distinct Numbers in Window")

A = [1, 2, 1, 3, 4, 3]
B = 3
distinct_number_in_window(A,B)



start_new("Max Sum Contiguous Subarray")

def max_sum_subarray(A):
    csum = 0
    msum = float("-inf")

    for num in A:
        csum += num 
        msum = max(msum , csum)

        if csum < 0:
            csum = 0
    
    print(f"max possible sum is :{msum}")

A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
max_sum_subarray(A)


def rain_water_trapped(A):
    # get the max on the both left and right 
    # Get the min of min(letf_max, right_max) - A[i]
    # if prev step answer > 0 , add to final answer 

    n = len(A)
    print()
    l_max,r_max = [0]*n , [0]* n
    l_max[0] = A[0]

    for i in range(1,n):
        l_max[i] = max(l_max[i-1] , A[i])
    print(f"Array is :{A}")
    print(f"Left max array is : {l_max}")

 
    r_max[n-1] = A[n-1]
    for i in range(n-2,-1,-1):
        r_max[i] = max(r_max[i+1] , A[i])
    
    print(f"Right max array is : {r_max}")
    ans = 0
    for i in range(1,n-1):
        water = min(l_max[i],r_max[i]) - A[i]
        if water > 0 :
            ans += water
    
    print(f"Final answer is {ans}")



start_new("Rain Water Trapped")
A = [5, 4, 1, 4, 3, 2, 7]
rain_water_trapped(A)