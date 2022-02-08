num = int(input())
def fib():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b
gen = fib()
for i in range(num):
	print(next(gen))