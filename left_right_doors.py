'''
Problem Statement:

There are exactly two exits from Shivraj's house, left and right exits. There are several doors in
each of the exits, so each door in Shivraj's house is located either in the left or in the right exit.
Initially all the doors are closed. Now Rahul, the friend of Shivraj is given a sequence in which
Shivraj opened the doors, please find the smallest index k such that Shivraj can exit the house
after opening the first k doors.He opened each door at most once, and in the end all doors
became open.

Note: Shivraj can exit the home, only if either all the left doors are open or all the right doors
are open

Input Format:

The first line contains an integer n (2≤n≤200000) which are the number of doors.
The next line contains n integers, the sequence in which Shivraj opened the doors.
The i-th of these integers is equal to 0 if the i-th opened door is located in the left exit, and it
is equal to 1 if it is in the right exit.It is guaranteed that there is at least one door located in the
left exit and there is at least one door located in the right exit.

Constraints:

(2≤n≤200000)

Output Format:

Print the smallest integer k such that after he opened the first k doors, he was able to exit the
house

'''

no_of_doors=int(input())
doors=list(map(int,input().split()))
right=doors.count(1)
left=no_of_doors-right
count=0
door=iter(doors)
while(right and left):
  x=next(door)
  if(x==1):
    right-=1
  else:
    left-=1
  count+=1
print(count)
