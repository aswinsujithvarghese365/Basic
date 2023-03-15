"""Problem
Given A,B, and C as the sides of a triangle, find whether the triangle is scalene.

Note:
A triangle is said to be scalene if all three sides of the triangle are distinct.
It is guaranteed that the sides represent a valid triangle.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of three space-separated integers A,B, and C — the length of the three sides of the triangle.

Output Format
For each test case, output on a new line, YES, if the triangle is scalene, and NO otherwise.
You may print each character of the string in uppercase or lowercase. For example, YES, yes, Yes, and yEs are all considered identical."""

# cook your dish here
T = int(input())
for i in range(T):
    tri = []
    tri = [int(x) for x in input().split()]
    if(tri[0]==tri[1] or tri[1]==tri[2] or tri[0]==tri[2]):
        print("NO")
    else:
        print("YES")
