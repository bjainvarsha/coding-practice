class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class Single_LL:
	def __init__(self):
		self.head = None
		self.tail = None

	def print_LL(self):
		if not self.head:
			print("Linked List Empty")
			return
		temp = self.head
		LL_string = "\n"		
		while temp:
			LL_string += str(temp.data) + " --> "
			temp = temp.next
		LL_string = LL_string[:-4] + "\n"
		if self.head:
			LL_string += "Head = " + str(self.head.data) + "\n"
		if self.tail:
			LL_string += "Tail = " + str(self.tail.data) + "\n"
		print(LL_string)
		count = self.length()
		print("Length of LL = " + str(count))


	def insert_end(self, data):
		if self.tail:
			self.tail.next = Node(data)
			self.tail = self.tail.next
		else:
			self.head = self.tail = Node(data)

	def insert_begin(self, data):
		if self.head:
			temp = Node(data)
			temp.next = self.head
			self.head = temp
		else:
			self.head = self.tail = Node(data)

	def insert_list_end(self, list_values):
		for data in list_values:
			self.insert_end(data)

	def insert_list_begin(self, list_values):
		for data in list_values[::-1]:
			self.insert_begin(data)

	def delete_begin(self):
		if self.head:
			if self.head.next:
				data = self.head.data
				self.head = self.head.next
			else:
				data = self. head.data
				self.head = self.tail = None
			return data
		else:
			print("Linked List is empty")
			return None

	def delete_end(self):
		if self.head:
			if self.head.next:
				temp = self.head
				while temp.next != self.tail:
					temp = temp.next
				data = self.tail.data
				self.tail = temp
				self.tail.next = None
			else:
				data = self.head.data
				self.head = self.tail = None
			return data
		else:
			print("Linked List is empty")
			return None

	def length(self):
		if not self.head:
			return 0
		else:
			count = 0
			temp = self.head
			while temp:
				count += 1
				temp = temp.next
			return count

	def search(self, data):
		if not self.head:
			return False
		else:
			temp = self.head
			while temp:
				if temp.data == data:
					return True
				temp = temp.next
			return False

	def get_nth_node(self, n):
		if not self.head:
			return None
		else:
			count = 0
			temp = self.head
			while temp:
				count += 1
				if count == n:
					return temp.data
				temp = temp.next
			return None

	def get_nth_node_end(self, n):
		if not self.head:
			return None
		else:
			count = n
			temp = self.head
			temp1 = self.head
			while count:
				count -= 1
				if not temp:
					return None
				else:
					temp = temp.next
			if count == 0:
				while temp and temp1:
					temp = temp.next
					temp1 = temp1.next
				if temp1:
					return temp1.data
				else:
					return None

	def get_middle_node(self):
		if not self.head:
			return None
		elif self.head and self.head.next:
			slow = self.head
			fast = self.head
			while slow and fast and fast.next:				
				slow = slow.next
				fast = fast.next.next
			if slow:
				return slow.data
			else:
				return None
		else:
			return self.head.data

	def reverse_LL(self):
		if not self.head:
			return None 
		else:
			reversed_LL = Single_LL()
			temp = self.head
			while temp:
				reversed_LL.insert_begin(temp.data)
				temp = temp.next
			return reversed_LL


	def isEmpty(self):
		if not self.head:
			return True
		else:
			return False

	def get_head(self):
		if not self.head:
			return None
		else:
			return self.head

def detect_loop(linked_list):
	if not linked_list.isEmpty():
		slow = linked_list.get_head()
		fast = linked_list.get_head().next
		print(slow.data)
		while slow and fast and fast.next:
			if slow == fast:
				return True
			slow = slow.next
			fast = fast.next.next
		return False
		






if __name__ == '__main__':
	LL = Single_LL()	
	LL.insert_list_begin([10])
	LL.print_LL()
	# print(LL.get_middle_node())
	reverse_LL = Single_LL()
	reverse_LL = LL.reverse_LL()
	reverse_LL.print_LL()
	LL.print_LL()
	LL.tail.next = LL.head
	print(detect_loop(LL))



