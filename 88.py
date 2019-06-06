import math
num1,num2=map(int,input().split())
num3=(num1*num2)/math.gcd(num1,num2)
print(int(num3))
