#reversing a string using list comprehension

def reverse(s):
    res=[s[i] for i in range(len(s)-1,-1,-1)]#begin,end-1,step ex; kumar , 4 to -1 , means 4th index to 0th index in reverse direction
    return "".join(res)
s=input()
print(reverse(s))

#time complexity O(n)
#space complexity O(1)