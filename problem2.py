names=input().split(",")
l=len(names)
for i in range(l):
	c=names[i].split(" ")
	for j in range(len(c)):
		print(c[j][0],end="")
	print(end="\n")