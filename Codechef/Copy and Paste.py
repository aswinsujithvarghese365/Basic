"""Problem
Chef has binary string A of length N. He constructs a new binary string B by concatenating M copies of 
A together. For example, if A="10010", M=3, then B="100101001010010".Chef calls an index (1≤i≤N⋅M) good if:
-> pref = suf + 1
Here, pref = B1 + B2 + B3 +.....+ Bj and suf = Bj + Bj+1 +.....+ BN.M
(Note that suf = N⋅M+1 = 0 by definition)

Chef wants to find the number of good indices in B. Can you help him do so?

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first line of each test case contains two space-separated integers N and M — the length of the binary string 
A and the number of times A is concatenated to form $
The second line of each test case contains a binary string A of length N containing 0s and 1s only.

Output Format
For each test case, output the number of good indices in B."""

for _ in range(int(input())):
    N,M=map(int,input().split(" "))
    A=input()
    S=[]
    total=0
    
    for i in range(N):
        total+=int(A[i])
        S.append(total)
    res=0
    
    if total==0:
        print(N*M)
    elif (M*total)%2 ==1:
        print(0)
    else:
        for j in range(M):
            pref=j*total
            suf=(M-j-1)*total
            if abs(suf-pref)<=total:
                for i in range(N):
                    if pref+int(S[i])==suf+total-int(S[i]):
                        res+=1
        print(res)
        
