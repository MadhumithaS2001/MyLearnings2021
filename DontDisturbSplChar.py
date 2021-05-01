'''
Question:


'''

'''

alternate:


import re
s=input().strip()

r=re.findall("[a-zA-Z]",s)
r.reverse()

out=""
j=0
for i in s:
  if(i not in "qwertyuiopasdfghjklzxcvbnmQWERTAYUIOPSDZFXCGVHBJNKML"):
    out+=i
  else:
    out+=r[j]
    j+=1
print(out.strip())


'''

import re
st=input().strip()
r=re.findall("[a-zA-Z]",st)
r.reverse()
#sp=r'[@_!\#$%^&*()<>?/|}{~:]'
al='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(st)):
    if(st[i] not in al):
        r.insert(i,st[i])
print(''.join(r))
