T = int(input(""))
L = []
c = []
d = []
c1 = 0
d1 = 0
for i  in range(0,T):
    vote = str(input(""))
    L.append(vote)
for j in range(0,T):
    vote_len = len(L[j])
    for k in range(0,vote_len):
        if(L[j][k] == "c"):
            c1+=1
        elif(L[j][k] == "d"):
            d1+=1
    c.append(c1)
    d.append(d1)
    c1=0
    d1=0
    
for l in range(0,T):
    c[l] = c[l] - d[l]
    if(c[l]>d[l]):
        print("cats")
    elif(c[l] == d[l]):
        print("tie")
    else:
        print("dogs")
