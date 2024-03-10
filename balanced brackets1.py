#check for balances brackets in an expression
#using stack LIFO ( Last In First Out)

def brackets(s):
    stack=[] #defining an empty stack
    for chr in s: #iterating every character in a string 
        if chr in ('(',"[","{"): #finding the opened bracket characters in a given string
            stack.append(chr) #adding the character in the stack
        else:
            if stack and (stack[-1]=="(" and chr==")") or (stack[-1]=="[" and chr=="]") or (stack[-1]=="{" and chr=="}"):#stack: checking whether the stack is not empty or not,
                 #AND also considering whether the last character is matched with the respetive closed bracket or not
                stack.pop()#if the respective character found then remove the lastly inserted bracket(character) from the stack
            else:
                return False
    return not stack #at final if the stack is empty then return true 
s=input()
if brackets(s):
    print("balanced")
else:
    print("not balanced")

#time complexity O(n)
#space complexity O(1)