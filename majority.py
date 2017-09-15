import collections
def majorityElement(nums):
	results = collections.defaultdict(int)
	for num in nums:
	    results[num] += 1

	val = max(results.items(), key=lambda x: x[1])[0]
	print(val)
	if val > (len(nums)/2):
	    return val

print(majorityElement([3,2,3]))
