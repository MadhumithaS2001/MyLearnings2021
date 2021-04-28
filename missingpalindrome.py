'''
This is a program to print the missing letter that tend to form the pallindrome string
'''

s=input()
s1=s[::-1]
for i in range(len(s)//2):
    print(s[i],s1[i])
    if(s1[i]!=s[i]):
        s2=s[i:len(s)-i]
        break
if(s2[1:]==s2[:0:-1]):
    print(s2[0])
else:
    print(s2[-1])
