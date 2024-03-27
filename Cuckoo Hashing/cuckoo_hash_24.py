# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List, Optional

class CuckooHash24:
	def __init__(self, init_size: int):
		self.__num_rehashes = 0
		self.bucket_size = 4
		self.CYCLE_THRESHOLD = 10
		self.table_size = init_size
		self.tables =  [[None]*init_size for _ in range(2)]
			
		

	def get_rand_idx_from_bucket(self, bucket_idx: int, table_id: int) -> int:
		# you must use this function when you need to displace a random key from a bucket during insertion (see the description in requirements.py). 
		# this function randomly chooses an index from a given bucket for a given table. this ensures that the random 
		# index chosen by your code and our test script match.
		# 
		# for example, if you are inserting some key x into table 0, and hash_func(x, 0) returns 5, and the bucket in index 5 of table 0 already has 4 elements,
		# you will call get_rand_bucket_index(5, 0) to determine which key from that bucket to displace, i.e. if get_random_bucket_index(5, 0) returns 2, you
		# will displace the key at index 2 in that bucket.
		rand.seed(int(str(bucket_idx) + str(table_id)))
		return rand.randint(0, self.bucket_size-1)

	def hash_func(self, key: int, table_id: int) -> int:
		key = int(str(key) + str(self.__num_rehashes) + str(table_id))
		rand.seed(key)
		return rand.randint(0, self.table_size-1)

	def get_table_contents(self) -> List[List[Optional[List[int]]]]:
		# the buckets should be implemented as lists. Table cells with no elements should still have None entries.
		return self.tables

	# you should *NOT* change any of the existing code above this line
	# you may however define additional instance variables inside the __init__ method.

	def insert(self, key: int) -> bool:
		if self.number_of_evictions >= self.CYCLE_THRESHOLD:
			return False
		
		index = self.hash_func(key, 0)
		if self.tables[0][index] is None:
			res = []
			# print(f"updating tables[0][{index}] with {key}")
			res.append(key)
			self.tables[0][index] = res
			self.number_of_evictions = 0
			# print(f"Reset evicted Value")
			# print(self.get_table_contents())
			return True
		
		list_in_index = self.tables[0][index]
		if len(list_in_index) != self.bucket_size:
			list_in_index.append(key)
			return True
		else:
			self.number_of_evictions += 1
			# print(f'Evictions are incremented {self.number_of_evictions} as tables[0][{index}] is not empty')
			h1_list = self.tables[0][index]
			h1_randIndex_replace = self.get_rand_idx_from_bucket(index,0)
			# print(f'Evicted Key {h1_evicted_key} from h1 to update the slot with {key}')
			self.tables[0][index] = key
			index = self.hash_func(h1_evicted_key, 1)
			if self.tables[1][index] is None:
				# print(f"updating tables[1][{index}] with {h1_evicted_key}")
				self.tables[1][index] = h1_evicted_key
				# print(self.get_table_contents())
				return True
			else:
				self.number_of_evictions += 1
				if self.number_of_evictions > self.CYCLE_THRESHOLD:
					return False
				# print(f'Evictions are incremented {self.number_of_evictions} as tables[1][{index}] is not empty')
				h2_evicted_key = self.tables[1][index]
				# print(f'Evicted Key {h2_evicted_key} from h1 to update the slow with {h1_evicted_key}')
				self.tables[1][index] = h1_evicted_key
				return self.insert(h2_evicted_key)
	

	def lookup(self, key: int) -> bool:
		# TODO
		pass
		

	def delete(self, key: int) -> None:
		# TODO
		pass

	def rehash(self, new_table_size: int) -> None:
		self.__num_rehashes += 1; self.table_size = new_table_size # do not modify this line
		# TODO
		pass

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define


