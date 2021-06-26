s=input().strip()  # abcdef acefdb
n=len(s)
print(s[0:n:2],end='')
print(s[::-1][0:n:2])
