#reversing a given string 
#using recursive method


def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:]) + s[0]#recursion happens 
s=input()
print(reverse(s))



#time complexity O(n)
#space complexity O(n)

#example = "saikumar"
#in 1st recursion --> reverse(aikumar)+s
#in 2nd recursion --> reverse(ikumar)



#i have to understand