def inverse_cascade(n):
	grow(n//10)
	print(n)
	shrink(n//10)

def grow(n):
	if n:
		grow (n//10)
		print(n)

def shrink(n):
	if n:
		print(n)
		shrink(n//10)
