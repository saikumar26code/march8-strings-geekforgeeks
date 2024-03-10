#Reversing of a given string using slice
def reverse(s):
    res=s[::-1]
    return res
string=input()
print(reverse(string))

#time complexity O(n)
#space complexity O(n)