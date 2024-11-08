
def start_new(func_name):
    import os 
    os.system("clear")
    print(f"Proessing for : {func_name}!!!\n")


def smallest_number(A):
    n = len(A)

    # Creating  freq array
    freq = [0]* 10

    print(A)

    # For each number element
    for ele in A:
        freq[ele] += 1
    print(freq)

    # For each number check the freq
    k = 0
    for i in range(10):
        temp_ferq = freq[i]
        for j in range(temp_ferq):
            A[k] = i
            k += 1
    
    print(f"samllest possible number is :{A}")


    

start_new("Smallest Number Using the Array")

A = [6,3,4,2,7,2,1]
smallest_number(A)


start_new("Smallest Number  Array with -ve values")

def smallest_no_negative(arr):
    # get length of freq array
    # create freq array - with value from the main array

    n = len(arr)

    min_v = min(arr)
    max_v = max(arr)

    freq_length = max_v - min_v + 1
    freq = [0]*freq_length
    print(f"max min freq {max_v , min_v , freq}")

    for i in range(n):
        freq[arr[i] - min_v] += 1
    print(freq)

    k = 0 
    for i in range(freq_length):
        temp_freq = freq[i]
        for j in range(temp_freq):
            arr[k] = i + min_v
            k += 1
    
    print(arr)
    

A = [-2,3,8,3,-2,3]
smallest_no_negative(A)
