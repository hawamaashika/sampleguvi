y=int(input())
if y%4==0 and y%100!=0:
	print(y,"is a leap year")
elif year%100==0:
	print(y,"is not a leap year")
elif year%400==0:
	print(y,"is a leap year")
else:
	print(y,"is not a leap year")
