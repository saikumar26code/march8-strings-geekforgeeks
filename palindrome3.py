def pali(s):
    rev="".join(reversed(s))
    if s==rev:
        return 'yes'
    return 'no'
s=input()
print(pali(s))