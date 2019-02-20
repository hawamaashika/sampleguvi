num=int(input())
if(num==2):
  print("it is prime")
elif num > 2:
  for i in range(2,num):
    if (num % i) == 0:
      print(" Not a prime")
      break
    else:
      print("yes")
      break
else:
  print("Not a prime")
