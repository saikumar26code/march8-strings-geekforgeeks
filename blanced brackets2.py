#check for balances brackets in an expression
#using the replace functin


# Observe the time and space complexity 


def brackets(s):
    while True:
        l=len(s)
        s=s.replace("()","")# replace function takes O(n) time 
        s=s.replace("[]","")
        s=s.replace("{}","")
        n=len(s)#every time new string is creating and the string is not stored permanently
        if n==l:
            break
    return "balanced" if len(s)==0 else "not balanced"#ternery operations
s=input()
print(brackets(s)) 


# i didn't get clarity on while loop 
#whether all statements should be executed or requires only one

#time complexty O(n^2)
#space complexity O(n)