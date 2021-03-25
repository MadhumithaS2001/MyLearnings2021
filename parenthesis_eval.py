brac=str(input())
li=[]
if(brac[0]==')'):
  print("no")
else:
  for i in brac:
    if(i=='('):
      li.append('(')
    elif(i==')' and len(li)>0):
      li.pop()
    else:
      li.append(')')
  if(len(li)==0):
    print("yes")
  else:
    print("no")
