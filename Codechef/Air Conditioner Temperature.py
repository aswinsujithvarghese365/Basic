"""Problem
There are three people sitting in a room - Alice, Bob, and Charlie. They need to decide on the temperature to set on the air conditioner. Everyone has a demand each:
Alice wants the temperature to be at least A degrees. Bob wants the temperature to be at most B degrees. Charlie wants the temperature to be at least C degrees. Can they all agree on some temperature, or not?

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line which contains three integers - A,B,C.

Output Format
For each test case, output on a new line, "Yes" or "No". "Yes", if they can decide on some temperature which fits all their demands. Or "No", if no temperature fits all their demands.
You may print each character of the string in either uppercase or lowercase (for example, the strings NO, nO, No, and no will all be treated as identical)."""

# cook your dish here
T = int(input())
for i in range(T):
    l = []
    l = [int(x) for x in input().split()]
    if(l[0]<=l[1] and l[2]<=l[1]):
        print("Yes")
    else:
        print("No")
