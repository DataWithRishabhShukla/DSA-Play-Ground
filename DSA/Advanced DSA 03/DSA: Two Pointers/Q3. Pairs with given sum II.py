
def find_pair_with_sum(A, B):
    n = len(A)
    s,e,count = 0,n-1, 0
    
    while s < e :
        sum = A[s] + A[e]

        if sum > B :
            print("Inside the sum > B Block !!! ")
            e -= 1 
        elif  sum < B :
            print("Inside the sum < B Block !!! ")
            s+=1

        else :
            # checking if there are no other elements in between 

            if A[s] == A[e]:
                print("Inside the A[s] == A[e] Block !!! ")
                total_elements = e - s + 1
                pairs = total_elements * (total_elements-1) / 2
                count += pairs
                break

            # Checking for the duplicates element 
            ps ,count_s = s , 0
            while A[ps] == A[s]:
                count_s += 1
                ps += 1
            
            pe , count_e = e , 0 
            while A[pe] == A[e] :
                count_e += 1
                pe -= 1
            count += count_e * count_s

            
         
    
    print(f"Number of pairs with {count}")

A = [1, 5, 7, 10]
B = 8
find_pair_with_sum(A,B)