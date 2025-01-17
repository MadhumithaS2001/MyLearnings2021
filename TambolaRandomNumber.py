import random
import time

box=list(range (1,91))
random.shuffle (box)

number_board_org = [[] for i in range(9)]
for i in range(9):
    number_board_org[i]= list(range(i*10+1,i*10+11))

print (*number_board_org ,sep="\n\n",end="\n\n") 

C=0
for i in box:
    C+=1
    print("\n",i,"\n")
    time.sleep(5)
    number_board_org [(i-1)//10][i%10-1]="--"
    if(C%10==0):
        print (*number_board_org,sep="\n\n")

print (number_board_org)
