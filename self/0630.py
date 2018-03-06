
def count(f):
        def counted(*args):
            counted.call_count += 1
            return f(*args)
        counted.call_count = 0
        return counted

fib = lambda n: 0 if n ==1 else 1 if n==2 else fib(n-2) + fib(n-1)

fib = count(fib)