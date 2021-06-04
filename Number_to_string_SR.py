'''
input 0:

121

output 0:

aba au la

input 1: 

12131

output 1:  

abaca abma auca laca lma

'''
def num_to_char(str1):
    if(str1==0):
        return ''
    return (chr(int(str1)+96))
        
n="12131"
list_of_words=[]

n_list=list(n)
def wordd(num):
    word=""
    for i in num:
        word+=(num_to_char(i))
    return(word)
res=wordd(n)
list_of_words.append(res.strip())
final=[]
for i in range(len(n)-1): #12131     
    finalval=(n[i:i+2])
    finalva=int(finalval)
    if(finalva>26):
        continue
    finalval1=n[:i]
    finalval2=n[i+2:]
    if(finalval1==None):
        finalval1=""
    else:
        finalval1=wordd(finalval1)
    if(finalval2==None):
        finalval2=""
    else:
        finalval2=wordd(finalval2)
    final.append(finalval)
    list_of_words.append(finalval1+num_to_char(finalval)+finalval2)
x=''
i=0
for j in range(len(n)-1):
    if(i<len(n)):
        y=int(n[i:i+2])
        if(y<27):
            x+=num_to_char(str(y))
            i+=2
        else:
            i+=1
list_of_words.append(x)
list_of_words=list(set(list_of_words))
list_of_words.sort()
print(*list_of_words)


#End of program
