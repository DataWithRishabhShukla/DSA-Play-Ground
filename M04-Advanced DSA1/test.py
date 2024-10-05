

A =[2,1,1,2,1]
B = [[1,5],[3,3],[2,4]]


def get_sum(A,B):
    n= len(A)
    psum_1 = [0]*n
    psum_2 = [0]*n

    psum_1[0] = 1 if A[0] ==1 else 0
    psum_2[0] = 1 if A[0] ==2 else 0
    # print(psum_1)
    # print(psum_2)

    for i in range(1,n):
        psum_2[i] = psum_2[i-1] +(1  if A[i] ==2 else 0)
        psum_1[i] = psum_1[i-1] +(1  if A[i] ==1 else 0)

    print(psum_1)
    print(psum_2)

    res = []
    print(B)
    print(len(B))
    print(B[0])
    print(B[0][0])
    print(B[0][1])
    for i in range(len(B)):
        print(f"\nCurr value of i :{i}")
        L = B[i][0] - 1
        R = B[i][1] - 1
        print(f"L,R : {L} {R}]")
        if L == 0:
            print(f"[L,R] : {[L,R]}")
            print(f"Final result : {[psum_1[R],psum_2[R]]}")
            res.append([psum_1[R],psum_2[R]])
        else:
            print(f"Final result : {psum_1[R]-psum_1[L-1],psum_2[R]-psum_2[L-1]}")
            res.append([psum_1[R]-psum_1[L-1],psum_2[R]-psum_2[L-1]])

    print(f"\n\n Anser is :{res}")



#get_sum(A,B)


def sum_of_digits(A):
    

    print(f"Num is :{A}")
    num = A
    res = []
    while A > 9 :
        digit = A %10
        res.append(digit)
        A = A //10
    
    res.append(A)
    print(res)
    s =  sum(res)

    print(f"\nSum is {sum(res)} \nnum is :{num} \nnum%s is : {num%s} ")

    if num % s == 0:
        print(s)
    else:
        print(-1)
    


# sum_of_digits(100)

def change_order(s,ch):
    st = list(s)
    si = 0 
    ei = float("-inf")
    print("\n\n")
    
    for i in range(len(st)):
        if st[i] == ch:
            ei = i
            break
    if ei < 0:
        print("char does not exist!! ")
        return s

    print(f"Values : {[si,ei]}")
    print(st[si:ei])
    print("".join(st))
    s,e = si , ei

    while si < ei :
        st[si],st[ei] = st[ei],st[si]
        si += 1
        ei -= 1

    print("\nAfter swap !!")
    print(st[s:e])
    print("".join(st))


change_order("hello world", "o" )
change_order("coding is love", "z" )

