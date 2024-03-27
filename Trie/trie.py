class TrieNode:
    def __init__(self, value=""):
        self.children = {}
        self.is_end_word = False
        self.value = value

class Trie:
    def __init__(self, is_compressed):
        self.is_compressed = is_compressed
        self.root = TrieNode()
        self.is_trie = True

    def construct_trie_from_text(self, text):
        """Constructs a trie from the given list of words."""
        self.is_trie = True
        if len(text) < 0:
            return -1
        for key in text:
            current_node = self.root
            # Insert key into the trie
            for char in key:
                if char not in current_node.children:
                    current_node.children[char] = TrieNode(char)
                current_node = current_node.children[char]
            current_node.is_end_word = True
        if self.is_compressed:
            self.compress_trie(self.root)

    def compress_trie(self, current_node: TrieNode, parent=None, char=None):
        """Compresses the trie recursively."""
        while len(current_node.children) == 1 and not current_node.is_end_word:
            next_node = next(iter(current_node.children.values()))
            current_node.value += next_node.value  # Concatenate labels
            current_node.is_end_word = next_node.is_end_word  # Preserve end of word flag
            # Update children
            current_node.children = next_node.children
            if parent:
                parent.children[char] = current_node
        for char, child in list(current_node.children.items()):
            # Recursively compress the child nodes
            self.compress_trie(child, current_node, char)
        current_node.is_end_word = True

    def construct_suffix_tree_from_text(self, keys: list[str]):
        for key in keys:
            for i in range(len(key)):
                key1 = key[i:]
                current_node = self.root
                # Insert each suffix into the suffix tree
                for char in key1:
                    if char not in current_node.children:
                        current_node.children[char] = TrieNode(char)
                    current_node = current_node.children[char]
                current_node.is_end_word = True
        if self.is_compressed:
            self.compress_suffix(self.root)

    def compress_suffix(self, current_node: TrieNode, parent=None, char=None):
        while len(current_node.children) == 1 and not current_node.is_end_word:
            next_node = next(iter(current_node.children.values()))
            current_node.value += next_node.value
            current_node.is_end_word = next_node.is_end_word  # Preserve end of word flag
            # Update children
            current_node.children = next_node.children
            if parent:
                parent.children[char] = current_node
        for char, child in list(current_node.children.items()):
            # Recursively compress child nodes
            self.compress_suffix(child, current_node, char)



    def search_and_get_depth(self, key):
        current_node = self.root
        depth = 0
        i = 0
        while i < len(key):
            flag = False
            for x, child in current_node.children.items():
                if key[i : i + len(child.value)] == child.value:
                    flag = True
                    depth = depth + 1
                    current_node = child
                    i = i + len(child.value)
                    break
            if not flag:
                return -1
        return depth