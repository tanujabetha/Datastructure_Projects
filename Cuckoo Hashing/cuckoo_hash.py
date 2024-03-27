# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List, Optional


class CuckooHash:
    def __init__(self, init_size: int):
        self.__num_rehashes = 0
        self.CYCLE_THRESHOLD = 10
        self.number_of_evictions = 0
        self.table_size = init_size
        self.tables = [[None] * init_size for _ in range(2)]

    def hash_func(self, key: int, table_id: int) -> int:
        key = int(str(key) + str(self.__num_rehashes) + str(table_id))
        rand.seed(key)
        return rand.randint(0, self.table_size - 1)

    def get_table_contents(self) -> List[List[Optional[int]]]:
        return self.tables

    def is_full_list(self, my_list) -> bool:
        if my_list is not None and not my_list:
            return True
        return False
    
    def insert1(self, key: int) -> bool:
        if self.lookup(key):
            return False  # If already there, return False (no duplicates)

        n = key
        for _ in range (int((self.CYCLE_THRESHOLD/2))):
            print(f'Key is:{key}')
            position1 = self.hash_func(n, 0) # Hash
            print(f'considering tables[0][{position1} for {key}')
            if self.tables[0][position1] is None:
                        self.tables[0][position1] = n
                        print(self.get_table_contents())
                        return True
            print(f'hash1 is not empty for index tables[0]{position1}')
            temp = self.tables[0][position1]
            self.tables[0][position1] = n
            n = temp
            position2 = self.hash_func(n, 1) 
            print(f'considering tables[1][{position1} for {key}')
            if self.tables[1][position2] is None:
                        self.tables[1][position2] = n
                        print(self.get_table_contents())
                        return True
            else:
                        temp = self.tables[1][position2]
                        self.tables[1][position2] = n
                        n = temp
            print(self.get_table_contents())
        return False
    
    def insert(self, key: int) -> bool:
        if self.number_of_evictions >= self.CYCLE_THRESHOLD:
            return False
        index = self.hash_func(key,0)
        if self.tables[0][index] is None:
            print(f"updating tables[0][{index}] with {key}")
            self.tables[0][index] = key
            self.number_of_evictions = 0
            print(f"Reset evicted Value")
            print(self.get_table_contents())
            return True
        else:
            self.number_of_evictions += 1
            print(f'Evictions are incremented {self.number_of_evictions} as tables[0][{index}] is not empty')
            h1_evicted_key = self.tables[0][index]
            print(f'Evicted Key {h1_evicted_key} from h1 to update the slot with {key}')
            self.tables[0][index] = key
            index = self.hash_func(h1_evicted_key, 1)
            if self.tables[1][index] is None:
                print(f"updating tables[1][{index}] with {h1_evicted_key}")
                self.tables[1][index] = h1_evicted_key
                print(self.get_table_contents())
                return True
            else:
                self.number_of_evictions += 1
                if self.number_of_evictions > self.CYCLE_THRESHOLD:
                    return False
                print(f'Evictions are incremented {self.number_of_evictions} as tables[1][{index}] is not empty')
                h2_evicted_key = self.tables[1][index]
                print(f'Evicted Key {h2_evicted_key} from h1 to update the slow with {h1_evicted_key}')
                self.tables[1][index] = h1_evicted_key
                return self.insert(h2_evicted_key)

    def lookup(self, key: int) -> bool:
        for row in range(len(self.tables)):
            for col in range(len(self.tables[row])):
                if self.tables[row][col] == key:
                    return True
        return False

    def delete(self, key: int) -> None:
        for row in range(len(self.tables)):
            for col in range(len(self.tables[row])):
                if self.tables[row][col] == key:
                    self.tables[row][col] = None

    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define

    def rehash(self, new_table_size: int) -> None:
        self.number_of_evictions = 0
        self.__num_rehashes += 1  # Increment the rehash counter
        self.table_size = new_table_size  # Set the new table size (do not modify this line)
        self.tables_temp = self.tables
        self.tables = [[None] * new_table_size for _ in range(2)]
        for i in range(len(self.tables_temp)):
            for j in range(len(self.tables_temp[i])):
                if self.tables_temp[i][j] is not None:
                    key = self.tables_temp[i][j]
                    self.insert(key)  
        #self.tables = self.tables_temp