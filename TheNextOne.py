'''
Implement the next permutation, which rearranges the list of numbers into Lexicographically next greater permutation of list of numbers. If such arrangement is not possible, it must be rearranged to the lowest possible order i.e. sorted in an ascending order. You are given an list of numbers arr[] of size N.

It is guranteed that such a solution will always exist.

Input Format

First line contains N, the size of array. Next line contains n integers,the elements of the array.

Constraints

1 ≤ N,A[i] ≤ 10000

Output Format

As mentioned in the problem statement.

Sample Input 0

6
1 2 3 6 5 4
Sample Output 0

1 2 4 3 5 6
Sample Input 1

3
3 2 1
Sample Output 1

1 2 3
'''


class Solution(object):
   def nextPermutation(self, nums):
      found = False
      i = len(nums)-2
      while i >=0:
         if nums[i] < nums[i+1]:
            found =True
            break
         i-=1
      if not found:
         nums.sort()
      else:
         m = self.findMaxIndex(i+1,nums,nums[i])
         nums[i],nums[m] = nums[m],nums[i]
         nums[i+1:] = nums[i+1:][::-1]
      return nums
   def findMaxIndex(self,index,a,curr):
      ans = -1
      index = 0
      for i in range(index,len(a)):
         if a[i]>curr:
            if ans == -1:
               ans = curr
               index = i
            else:
               ans = min(ans,a[i])
               index = i
      return index
ob1 = Solution()
N=int(input())   #len(A)
A=list(map(int,input().split()))  # [1,2,3,4,5,6]
print(*(ob1.nextPermutation(A)))
