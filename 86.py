num1=input().split()
for x in num1:
	s=set(x)
	if leng(s) == leng(x):
		print("Yes")
	else:
		print("No")
