def pali(s):
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-1-i]:
            return 'no'
    return 'yes'
s=input()
print(pali(s))