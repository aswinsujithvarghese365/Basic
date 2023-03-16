"""Problem
Vasya likes the number 239. Therefore, he considers a number pretty if its last digit is 2, 3 or 9.
Vasya wants to watch the numbers between L and R (both inclusive), so he asked you to determine how many pretty numbers are in this range. Can you help him?

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains two space-separated integers L and R.

Output
For each test case, print a single line containing one integer — the number of pretty numbers between L and R."""

# cook your dish here
k=0
T = int(input())
for i in range(T):
    l = []
    l = [int(x) for x in input().split()]
    l = [int(x) for x in range(l[0],l[1]+1)]
    l2 = [str(y) for y in l]
    for j in range(0,len(l2)):
        if(l2[j][-1]=="2" or l2[j][-1]=="3" or l2[j][-1]=="9"):
            k+=1
    print(k)
    k=0
