def fb(x):
	if x == 1:
		return 0
	elif x == 2:
		return 1
	else:
		return fb(x-1)+fb(x-2)



g = lambda x: 0 if x==1 else 1 if x == 2 else g(x-1) + g(x-2)

h = lambda x: 1 if x==0 else x*h(x-1)


def sum_digits(n):
	if n < 10:
		return n
	else:
		return sum_digits(n//10) + n%10

def reverse(word):
	if len(word) < 2:
		return word
	else:
		return reverse(word[1:]) + word[0]

def minimum(lst):
	if len(lst) == 1:
		return lst[0]
	if len(lst) == 2:
		return min(lst[0],lst[1])
	else:
		return minimum([minimum(lst[1:]),lst[0]])


