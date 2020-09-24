d.i=1
d.j=2
d.k=3
str = ["1","2","3"]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])