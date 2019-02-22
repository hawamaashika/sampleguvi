f=int(input())
g=int(input())

for n in range(f+1,g):
	sum=0
	temp=n
	while temp > 0 :
		r=temp%10
		sum=sum+(r**3)
		temp=temp//10
	if sum==n:
		print(sum)
