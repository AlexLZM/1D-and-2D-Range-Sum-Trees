class BIT():

	def __init__(self, arr):
		'''
		initialize the tree with a array
		'''
		self.n = len(arr)
		self.tree = [0] * (self.n + 1) # 1 dummy element for 1-index

		for i in range(n):
			self.update(i, arr[i])

	def update(self, i, diff):
		'''
		update the value at original array's index i by a difference
		'''
		i += 1 # convert to 1-index
		while i <= self.n:

			self.tree[i] += diff
			i += (i & (-i))

	def query(self, i):
		'''
		Get the sum of range [0,i]
		(including i)

		'''
		i += 1 # convert to 1-index
		res = 0
		while i>0:
			res += self.tree[i]
			i -= (i & (-i))
		return res

