a,b=map(int,input().split())
aa,bb=a,b

while bb!=0:
    aa=aa%bb
    aa,bb=bb,aa

c=a*b//aa

print(aa)
print(c)