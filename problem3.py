#using recurssion
def gcd(c,d):
	e=c-d
	if(e>d):
		c=e
		gcd(c,d)
	elif(e==d):
		print("GCD is",e)
	else:
		c=d
		d=e
		gcd(c,d)

a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if(a>b):
	gcd(a,b)
else:
	gcd(b,a)