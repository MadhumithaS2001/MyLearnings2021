'''
Problem Statement

Given a stack of integers, write a function checkpairconsecutive() that checks whether
numbers in the stack are pairwise consecutive or not. The pairs can be increasing or
decreasing, and if the stack has an odd number of elements, the element at the top is left out
of a pair. The function should retain the original stack content.

Input Format

Read the numbers in the stack.

Output Format

Check whether the stack elements are pairwise consecutive or not

'''
def fun(l):
  for i in range(0,len(l),2):
    if(l[i]!=(l[i+1]-1)):
      return "No"
  return "Yes"
l=list(map(int,input().split()))
print(fun(l))
