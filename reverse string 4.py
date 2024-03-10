#reversing a string using reversed fumction 

#reversed function returns a new object 

def reverse(s):
    res="".join(list(reversed(s)))# we can also write like res="".join(reversed(s))
    return res
s=input()
print(reverse(s))

#time complexity O(n)
#space complexity O(1)