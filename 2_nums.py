def two_nums(arr, total):
	seen = set()
	for val in arr:
		target = total - val
		if target not in seen:
			seen.add(val)
		else:
			return (val, target)
	return 'No matches' 
		
print(two_nums([1,2,3], 6))

