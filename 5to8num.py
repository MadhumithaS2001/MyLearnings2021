'''
Problem Statement:

A list of numbers will be given, the numbers 5 and 8 are present in the (8 always comes
after 5) problem.

Input Format:

Num1 : Add all numbers which do not lie between 5 and 8(excluding 5 and 8)
Num2 : Numbers formed by concatenating all numbers from 5 and 8(including 5 8)

Output Format:

Num1: 3+2+6+9=20
Num2: ‘5’+’1’+’4’+’8’=5148
condition2: 5148+20=5168

'''



a=list(map(int,input().split(',')))
f=a.index(5)
e=a.index(8)
s=sum(a[:f]+(a[e+1:]))
print((int("".join(str(x) for x in a[f:e+1])))+s)
