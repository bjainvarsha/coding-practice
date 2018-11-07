def findMedian(arr):
	sorted(arr)
	n = len(arr)
	if n%2 == 0:
		return float((arr[int(n/2)] + arr[int(n-1/2)])/2.0)
	else:
		return float(arr[int(n/2)])
if __name__ == '__main__':
	arr = [1,5,8,-1,100]
	print(findMedian(arr))

