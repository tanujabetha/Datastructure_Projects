from typing import TypeVar
import random
from zip_tree import ZipTree
from collections import deque

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class SkipList:
    def __init__(self):
        # Initialize an empty Skip List
        self.levels = 0
        self.lists = [ZipTree() for _ in range(self.levels + 1)]

    def get_random_level(self, key: KeyType) -> int:
        """Determine the level at which a key should be placed."""
        random.seed(str(key))
        level = 0
        while random.random() < 0.5 and level < 20:
            level += 1
        return level

    def insert(self, key: KeyType, val: ValType, rank: int = -1):
        level = self.get_random_level(key) if rank == -1 else rank
        if level > self.levels:
            self.levels = level
            self.lists.extend([ZipTree() for _ in range(self.levels - len(self.lists) + 1)])

        for i in range(level + 1):
            self.lists[i].insert(key, val)

    def remove(self, key: KeyType):
        for i in range(self.levels + 1):
            self.lists[i].remove(key)

    def find(self, key: KeyType) -> ValType:
        return self.lists[0].find(key)

    def get_list_size_at_level(self, level: int) -> int:
        if level <= self.levels:
            return self.lists[level].get_size()
        else:
            return 0

    def from_zip_tree(self, zip_tree: ZipTree) -> None:
        # Iterate through each level of the SkipList and insert nodes from the corresponding ZipTree
        for level in range(self.levels + 1):
            zip_tree_nodes = zip_tree.get_nodes_with_rank(level)
            for node in zip_tree_nodes:
                # Modify this line to insert key-value pairs as specified in the desired output
                self.insert(node.key, node.value, node.rank)