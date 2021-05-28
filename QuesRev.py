'''
Queue reverse in python using class
'''
class Queue:
  def __init__(self,list_of_items):
    self.elements=list_of_items
  def reverse_ele(self):
    return ''.join(self.elements[::-1])

list1=list(input())
obj1=Queue(list1)
print(obj1.reverse_ele())
