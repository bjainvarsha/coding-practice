class Heap:
	def __init__(self, isMinOrMax = "Min"):
		self._values = []
		if isMinOrMax == "Min":
			self._type = 0
		elif isMinOrMax == "Max":
			self._type = 1
		self._size = 0

	def parent(self, n):
		if n < self._size:
			return int((n-1)/2)
		elif n == 0 or n > self._size - 1:
			return None

	def insert(self, data):
		self._values.append(data)	
		self._size += 1
		n = self._size - 1
		print(self._values)
		if self._type:
			while n != 0 and self._values[self.parent(n)] < self._values[n]:
				print("Yes")
				self._values[self.parent(n)], self._values[n] = self._values[n], self._values[self.parent(n)]
				n = self.parent(n)

		elif not self._type:
			while n != 0 and self._values[self.parent(n)] > self._values[n]:
				print("Yes")
				self._values[self.parent(n)], self._values[n] = self._values[n], self._values[self.parent(n)]
				n = self.parent(n)

	def print(self):
		for i in self._values:
			print(str(i) + " ")

	def extractMin(self):
		n = self.

		


	def minHeapify(self):
		for i, val in enumerate(self._values):
			if self._size - 1 > ((2*i)) :
				if val > self._values[2*i + 1]:
					temp = val
					self._values[i] = self._values[2*i + 1]
					self._values[2*i + 1] = temp
			if self._size - 1 > ((2*i) + 1) :
				if val > self._values[2*i + 2]:
					temp = val 
					self._values[i] = self._values[2*i +2]
					self._values[2*i + 2] = temp
			print(self._values)




if __name__ == '__main__':
	heap = Heap("Max")
	heap.insert(1000)
	heap.insert(4)
	heap.insert(10)
	heap.insert(-9)
	heap.insert(100)
	heap.print()