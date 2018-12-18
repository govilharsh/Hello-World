a=input().split(",")
a=list(map(int,a))
a.sort()
b={}
for x in a:
	if x not in b:
		b[x]=1
	else:
		b[x]=b[x]+1
for i in b:
	print(i,"=",b[i])