def fib(n):
    """Compute the nth Fibonacci number, for n >= 2.

    >>>fib(2)
    1
    >>>fib(3)
    1
	>>>fib(50)
	7778742049
	"""
    pred, curr = 0, 1   # Fibonacci numbers 1 and 2
    k = 2               # Which Fib number is curr?
    while k < n:
         pred, curr = curr, pred + curr
         k = k + 1
    return curr
   
result = fib(8)


def count(s,value):
	"""Count the number of occurrences of value in sequence s."""
	total = 0
	for x in s:
		if x == value:
			total = total +1
	return total

threes=[[1,2,3],[4,5,6],[7,8,9],[1,1,1],[2,2,2],[3,3,3]]

	for x,y,z in s:
		if x == y and y ==z
		result += [x,y,z]
	return result









