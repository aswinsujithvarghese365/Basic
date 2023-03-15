"""Problem
Each pizza consists of 44 slices. There are N friends and each friend needs exactly X slices.
Find the minimum number of pizzas they should order to satisfy their appetite.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two integers N and X, the number of friends and the number of slices each friend wants respectively.

Output Format
For each test case, output the minimum number of pizzas required."""

# cook your dish here
import math as m
T = int(input())
for i in range(T):
    l = []
    l = [int(x) for x in input().split()]
    res = m.ceil((l[0]*l[1])/4)
    print(res)
