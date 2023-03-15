"""Problem
Chef has a bucket having a capacity of K liters. It is already filled with X liters of water.
Find the maximum amount of extra water in liters that Chef can fill in the bucket without overflowing.

Input Format
The first line will contain T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two space separated integers K and X - as mentioned in the problem.

Output Format
For each test case, output in a single line, the amount of extra water in liters that Chef can fill in the bucket without overflowing."""

# cook your dish here
T = int(input())
for i in range(T):
    l = []
    l = [int(x) for x in input().split()]
    res = l[0]-l[1]
    print(res)
