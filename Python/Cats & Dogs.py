T = int(input(""))
L = []
c = 0
d = 0
for i  in range(0,T):
    vote = str(input(""))
    L.append(vote)
for j in range(0,T):
    vote_len = len(L[j])
    for k in range(0,vote_len):
        if(L[j][k] == "c"):
            c+=1
        elif(L[j][k] == "d"):
            d+=1
    c-=d
    if(c > d):
        print("cats")
    elif(c == d):
        print("tie")
    else:
        print("dogs")
    c = 0
    d = 0
