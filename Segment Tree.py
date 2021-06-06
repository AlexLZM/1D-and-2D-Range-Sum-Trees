


class SegTree():

	def __init__(self, arr):
		'''
		initialize the tree with a array
		'''
		self.n = len(arr)
		self.tree = [0] * 2 * self.n
		self.tree[self.n: 2 * self.n] = arr

		# build the values backwards
		for i in range(n-1, 0, -1):
			# i<<1 = 2*i, i<<1|1 = 2*i+1
			self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]


	def update(self, i, value):
		"""
		update the value in the array at the index i
		"""
		i += self.n
		self.tree[i] = value

		while i > 1:
			# the parent value = current value + sibling value
			self.tree[i>>1] = self.tree[i] + self.tree[i^1]
			i >>= 1




	def query(self, start, end):
		'''
		query a sum of range of index [start, end) 
		(not including end)
		'''
		res = 0
		start += self.n
		end += self.n

		while start < end:
			if start & 1: # start is odd
				res += self.tree[start] # 
				start += 1 
			if end & 1: # edn is odd
				end -= 1
				res += self.tree[end]

			start >>= 1
			end >>= 1
		return res

