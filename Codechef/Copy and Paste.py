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
