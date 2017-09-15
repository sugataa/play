from collections import defaultdict
d = defaultdict()
def recursive_mem_fib(n):
	'''returns the nth fibonacci number'''
	# 0, 1, 1, 2, 3, 5, 8
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		if n in d:
			return d[n]
		d[n] = recursive_mem_fib(n-1) + recursive_mem_fib(n-2)
	return d[n]

def iterative_fib(n):
	'''returns the nth fibonacci number'''
	a, b = 0, 1
	for i in range(0, n):
		a, b = b, a+b
	return a

def recursive_fib_print(upper_bound):
	'''prints all fibonacci numbers less than upper bound'''
	val = 0
	i = 0
	while val < 1000:
		val = recursive_mem_fib(i)
		print(val)
		i += 1
	return

recursive_fib_print(4)

def iterative_fib_print(upper_bound):
	'''prints all fibonacci numbers less than upper bound'''
	a, b = 0, 1
	while a < upper_bound:
		print(a)
		a, b = b, a+b
	return
# print(fib(20))
# iterative_fib_print(14)
