n = int(input())
m = int(input())
k = int(input())
all = n*m
if k == (n-1)*m or all-(n-1)*m or n*(m-1) or all-n*(m-1):
	print("YES")
else:
	print("NO")