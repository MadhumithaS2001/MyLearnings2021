'''
Problem Statement:

Chandu is very hardworking and an intelligent guy. Chandu is a system administrator. There are
two servers under his strict guidance, a and b. Chandu executes commands "ping a" and "ping
b" to stay informed about the servers' performance. Each ping command sends exactly ten
packets to the server specified in the argument of the command. Executing a program results
in two integers m and l (m + l = 10; m, l ≥ 0). These numbers mean that m packets successfully
reached the corresponding server through the network and l packets were lost.
Today Chandu has performed overall n ping commands during his workday. Now for each
server Chandu wants to know whether the server is "alive" or not. Chandu thinks that the server
is "alive", if at least half of the packets that we send to this server reached it successfully along
the network.
Help Chandu, determine for each server, whether it is "alive" or not by the given commands and
their results.

Input Format:

First line contains an integer n is number of commands where (2 ≤ n ≤ 1000) and each of the n
lines contains 3 integers which are the description of the commands.
The i-th of these lines contains three space-separated integers ti, mi, li (1 ≤ ti ≤ 2; mi, li ≥ 0; mi +
li = 10).
The i-th command is "ping a" if ti = 1 else the i-th command is "ping b". After executing the
command, mi packets reached the corresponding server successfully and li packets were lost.
It is guaranteed that the input has at least one "ping a" command and at least one "ping b"
command.

Constraints:

(2 ≤ n ≤ 1000)
(1 ≤ ti ≤ 2; mi, li ≥ 0; mi + li = 10)

Output Format:

In the first line print string "LIVE" (without the quotes) if server a is "alive", otherwise print "DEAD" (without the quotes).
In the second line print the state of server b in the similar format.


'''


n=int(input())
ping={1:{'m':0,'l':0},2:{'m':0,'l':0}}
for i in range(n):
  x,y,z=map(int,input().split())
  ping[x]['m']+=y
  ping[x]['l']+=z
for i in range(1,3):
  m=ping[i]['m']
  l=ping[i]['l']
  if((m+l)//2<=m):
    print("LIVE")
  else:
    print("DEAD")
