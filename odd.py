s=int(input())
c=int(input())
print(str(s)+" "+str(c))
for i in range(s+1,c):
    if(i%2!=0):
        print(i)
