def closest_sum(arr, target):
	x = sorted(arr)
	left = 0
	right = len(x) - 1
	while left < right:
		sum_lr = x[left] + x[right]
		if sum_lr == target:
			print("found sum of " + str(x[left]) + " and " + str(x[right]))
			return
		elif sum_lr < target:
			left += 1
		else:
			right -= 1
	print("Not found")
if __name__ == '__main__':
	arr = [1,5,6,8,10]
	target = 7
	closest_sum(arr, target)