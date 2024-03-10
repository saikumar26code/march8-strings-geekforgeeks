#reversing a string using reverse function call
def reverse(s):
    res=list(s)
    res.reverse()
    return "".join(res)
s=input()
print(reverse(s))

#time complexity O(n)
#space complexity O(n)