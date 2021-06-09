'''
Problem Statement
Two players play a game.
Initially there are n integers a1,a2,…,an written on the board. Each turn a player selects one
number and erases it from the board. This continues until there is only one number left on the
board, i. e. n−1 turns are made. The first player makes the first move, then players alternate
turns.
The first player wants to minimize the last number that would be left on the board, while the
second player wants to maximize it.
You want to know what number will be left on the board after n−1 turns if both players make
optimal moves.
Input Format
The first line contains one integer n — the number of numbers on the board.
The second line contains n integers a1,a2,…,an .
Constraints
(1≤n≤1000) (1≤ai≤10^6)
Output Format
Print one number that will be left on the board.

IP:

3
2 1 3

OP: 

2

'''
no_of_numbers = int(input())
numbers = list(map(int, input().split()))
i = 0
while (i != no_of_numbers-1):
    i += 1
    if (i & 1):
        m = numbers.index(max(numbers))
        numbers.pop(m)
    else:
        m=numbers.index((min(numbers)))
        numbers.pop(m)
print(*numbers)
