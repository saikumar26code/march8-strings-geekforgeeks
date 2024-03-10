def pali(s):
    return s==s[::-1]
s=input()
res=pali(s)#i got new way of representation 
if res:
    print('yes')
else:
    print('no')