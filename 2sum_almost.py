def twosum_almost(arr, k):
    arr.sort()
    left_pointer, right_pointer = 0, len(arr)-1
    has_match = False
    almost_pair = None
    almost_sum = float('inf')
    while left_pointer < right_pointer:
        _sum = arr[left_pointer] + arr[right_pointer]
        if abs(k-_sum) < almost_sum:
            almost_sum = abs(k-_sum)
            almost_pair = (arr[left_pointer], arr[right_pointer])
        if _sum < k:
            left_pointer += 1
        elif _sum > k:
            right_pointer -= 1
        else:
            print((arr[left_pointer], arr[right_pointer]))
            left_pointer += 1
            has_match = True

    if not has_match:
        print(almost_pair)

arr = [1,2,3,-1]
k = -2
twosum_almost(arr, k)
