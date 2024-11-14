import os 

os.system("clear")

print("Section   - Advance DSA 02")
print("Module    - DSA: Stacks 1: Implementation & Basic Problems")
print("Problem 1 -  Balanced Paranthesis !!\n")


def check_parathesis(A):
    stk = []
    for ch in A :
        if ch in "{([":
            stk.append(ch)
        elif ch == "]" :
            if not stk or stk[-1] !="[":
                return 0
            stk.pop()
        elif ch == "}":
            if not stk or stk[-1] != "{":
                return 0 
            stk.pop()
        elif ch == ")":
            if not stk or stk[-1] != "(":
                return 0
            stk.pop()
        
    
    if stk :
        return 0
    else:
        return 1

A = "{([])}"
print(check_parathesis(A))

os.system("clear")

print("Section   - Advance DSA 02")
print("Module    - DSA: Stacks 1: Implementation & Basic Problems")
print("Problem 2 -  Double Character Trouble !!\n")

def double_character_trouble(A):
    stk = []  # initializing the stack 

    for ch in A :
        if not stk :
            stk.append(ch)
        elif ch == stk[-1]:
            stk.pop()
        else :
            stk.append(ch)

    print("".join(stk))

double_character_trouble("abccbc") 

os.system("clear")
print("Section   - Advance DSA 02")
print("Module    - DSA: Stacks 1: Implementation & Basic Problems")
print("Problem 2 -  Evaluate Expression !!\n")

def solve(A):
    stk = []

    for ch in A :
        if ch not in "+-*/":
            stk.append(ch)
        elif ch == "+":
            op2 = int(stk.pop())
            op1 = int(stk.pop())
            res = op1 + op2
            stk.append(res)
        elif ch == "-":
            op2 = int(stk.pop())
            op1 = int(stk.pop())
            res = op1 - op2
            stk.append(res)
        elif ch == "*":
            op2 = int(stk.pop())
            op1 = int(stk.pop())
            res = op1 * op2
            stk.append(res)
        elif ch == "/":
            op2 = int(stk.pop())
            op1 = int(stk.pop())
            res = op1 / op2
            stk.append(res)

    print(f"Final Result is :{stk[0]}")

A = ["2", "1", "+", "3", "*"]
A = ["4", "13", "5", "/", "+"]
solve(A)