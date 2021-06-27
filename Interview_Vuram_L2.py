'''
The program should print the count of the given word in the sentence 


Input:
 hi  hi hello ih  hi   mk o jk ok
hi

Output:
3

'''
s=input()
word=input()
i=0
leng=0
for j in s:
    leng+=1
l=[]
while(i<leng):
    x=''
    while(not(s[i] == ' ') and s[i]!='\n'):
        x+=s[i]
        i+=1
        if(i==leng):
            break
    if(x!=''):
        l.append(x)
    i+=1
count=0
#print(l)
for i in l:
    if(i==word):
        count+=1
print(count)



#end
