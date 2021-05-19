'''An array of N integers with non-zero values is passed as the input to the program. 
The program must print another array of size N where value at each index will be the product of all values 
in the input array except the value at that index in the input array.'''
def prd(lis):
    p=1
    for i in lis:
       p*=i
    return p
    
l=list(map(int,input().split()))
for i in range(len(l)):
    x=[]
    x.extend(l[i+1:])
    x.extend(l[:i])
    print(prd(x),end=" ")
