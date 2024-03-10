def pali(s):
    str=''
    for i in s:
        str=i+str
    if s==str:
        return 'yes'
    return 'no'
s=input()
print(pali(s))