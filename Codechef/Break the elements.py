"""Problem
Chef has an array A of length N. In one operation, Chef can choose any element Ai and split it into two positive integers 
X and Y such that X+Y=Ai. Note that the length of array increases by 1 after every operation.

Determine the minimum numbers of operations required by Chef to make parity of all the elements same.
It is guaranteed that parity of all the elements can be made equal after applying the above operation zero or more times.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains a single integer N — the length of array A.
Next line contains N space-separated integers A1, A2, A3, ......, An - denoting the array A.

Output Format
For each test case, output the minimum number of operations required to make parity of all elements same."""

# cook your dish here
T = int(input())
for i in range(T):
    ele = int(input())
    l = [int(x) for x in input().split()]
    p = 0
    for j in range(ele):
        if(l[j]%2==0):
            p+=1
    if(p==0 or p==ele):
        print(0)
    else:
        print(p)
