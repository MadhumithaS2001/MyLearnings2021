'''
3 3 4 10
  5 8 12
'''
lines=list(map(int,input().split()))
n=int(lines[0])
l=list(map(int, lines [1:]))
for i in l:
    s1=(str(bin(i)) [2:])
    l1=len(s1)
    one1, zero1= (s1.count('1'), s1.count('0'))
    one2, zero2 = (0, 0)
    x = i + 1
    print(s1)
    while (x <= i * 2):
        s2 = (str(bin(x))[2:])
        print(s2)
        one2, zero2 = s2.count('1'), s2.count('0')
        if ((one2==one1) and zero1<=zero2):
            print(x, "end")
            break
        x += 1
