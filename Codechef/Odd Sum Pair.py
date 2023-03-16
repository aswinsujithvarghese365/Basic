"""Problem
Chef has 3 numbers A,B and C.
Chef wonders if it is possible to choose exactly two numbers out of the three numbers such that their sum is odd.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of three integers A,B,C.

Output Format
For each test case, output YES if you can choose exactly two numbers with odd sum, NO otherwise.
The output is case-insensitive. Thus, the strings YES, yes, yeS, and Yes are all considered the same."""

# cook your dish here
T = int(input())
for i in range(T):
    l=[]
    l=[int(x) for x in input().split()]
    if((l[0]+l[1])%2!=0 or (l[0]+l[2])%2!=0 or (l[2]+l[1])%2!=0):
        print("YES")
    else:
        print("NO")
