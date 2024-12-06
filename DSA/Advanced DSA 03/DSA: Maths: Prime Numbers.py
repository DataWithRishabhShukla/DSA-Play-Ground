import os 

os.system("clear")

print("Section  - Advance DSA 03")
print("Module   - DSA: Maths: Prime Numbers")
print("Problem  - Get prime number in range !!\n")



def get_prime_in_range(A):

    prime = [True for _ in range(A+1)]
    print(prime)

    for i in range(2,A+1):
        if prime[i] == True :
            for j in range(2*i,A+1,i):
                prime[j] = False
    
    print(prime)
    for i in range(2,A+1):
        if prime[i] == True :
            print(i)


get_prime_in_range(10)



import os 

os.system("clear")

print("Section  - Advance DSA 03")
print("Module   - DSA: Maths: Prime Numbers")
print("Problem  - Count the number of factors !!\n")

def count_factors(N):

    fact = [2 for _ in range(N+1)]
    fact[0]  = 0
    fact[1]  = 1
    


    lst  = [i for i in range(11)]
    print(lst)
    print(fact, end="\n\n")
    

    for i in range(2,N+1):
        for j in range(2*i, N+1,i):
            fact[j] += 1
        print(fact)
    
    print(f"Sum of factors is : {sum(fact)}")

    print(fact)
count_factors(10) 
    

os.system("clear")
print("Section  - Advance DSA 03")
print("Module   - DSA: Maths: Prime Numbers")
print("Problem  - Sorted Permutation Rank !!\n")


def factorial(num):
    if num == 0 or num == 1 :
        return 1

    return num * factorial(num-1)

def sorted_permutaion_rank(ip):

    n = len(ip)
    ans = 0

    for i in range(n-1):
        
        ch = ip[i]
        print(f"Processing for the char :{ch}")

        smaller = 0
        
        for j in range(i+1,n):
            if ip[j] < ch :
                smaller += 1
        
        print(f"Value for the smaller for {ch} is :{smaller}\n")
        
        ans += smaller * factorial(n-i-1)
        #ans = ans % 1000003
    
    print(f"answer is :{ans+1}")


sorted_permutaion_rank("dfche")
    

        

        