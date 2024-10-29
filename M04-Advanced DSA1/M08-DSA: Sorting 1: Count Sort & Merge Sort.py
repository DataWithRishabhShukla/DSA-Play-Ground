
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

