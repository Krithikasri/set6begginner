nn=int(input())
i=0
while(nn>0):
	b=nn%10
	i+=b
	nn=nn//10
print(i)
