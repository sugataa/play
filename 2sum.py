def twosum(arr, k):
	seen = set()
	for num in arr:
		target = k - num
		if target not in seen:
			seen.add(num)
		else:
			print((num, target))

def twosum2(arr, k):
	# sort the array O(n*logn)
	arr.sort()
	# left, right pointer
	left_pointer = 0
	right_pointer = len(arr)-1
	# walk the list from left to right
	while left_pointer < right_pointer:
		_sum = arr[left_pointer] + arr[right_pointer]
		if _sum < k:
			left_pointer += 1
		elif _sum > k:
			right_pointer -= 1
		else:
			print((arr[left_pointer], arr[right_pointer]))
			left_pointer += 1
arr = [1,7,2,3,6]
k = 9
twosum2(arr, k)
