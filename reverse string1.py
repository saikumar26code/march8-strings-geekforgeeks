#reverse the string
#using a loop

#Oberve the time and space complexity 

def revers(s):
    str="" #definning the empty string
    for i in s:# iterating each char in input string  not in str
        str=i+str#concatinating the iterating character and empty string
    return str
s=input()
print(revers(s))

#time complexity O(n^2)(n*k)
#space complexity O(n)