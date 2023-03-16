"""Problem
There are N cards on a table, out of which X cards are face-up and the remaining are face-down.
In one operation, we can do the following:
Select any one card and flip it (i.e. if it was initially face-up, after the operation, it will be face-down and vice versa)
What is the minimum number of operations we must perform so that all the cards face in the same direction (i.e. either all are face-up or all are face-down)?

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains two space-separated integers N and X — the total number of cards and the number of cards which are initially face-up.

Output Format
For each test case, output the minimum number of cards you must flip so that all the cards face in the same direction."""

# cook your dish here
T = int(input())
for i in range(T):
    l=[]
    l=[int(x) for x in input().split()]
    if(l[1]==0 or l[1]==l[0]):
        print(0)
    elif(l[1]<(l[0]/2)):
        res = l[1]
        print(res)
    else:
        res = l[0]-l[1]
        print(res)
