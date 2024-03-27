class TrieNode:
    def __init__(self, value=""):
        self.children = {}
        self.is_end_of_word = False
        self.value = value

class Trie:
    def __init__(self, is_compressed):
        self.is_compressed = is_compressed
        self.root = TrieNode()
        self.is_trie = True

    def construct_trie_from_text(self, text):
        """Constructs a trie from the given list of text."""
        if not text:
            return -1
        for word in text:
            current_node = self.root
            for char in word:
                if char not in current_node.children:
                    current_node.children[char] = TrieNode(char)
                current_node = current_node.children[char]
            current_node.is_end_of_word = True
        if self.is_compressed:
            self.compress_trie(self.root)

    def compress_trie(self, node: TrieNode, parent=None, char=None):
        """Compresses the trie recursively."""
        while len(node.children) == 1 and not node.is_end_of_word:
            next_node = next(iter(node.children.values()))
            node.value += next_node.value  # Concatenate values
            node.is_end_of_word = next_node.is_end_of_word  # Preserve end of word flag
            node.children = next_node.children  # Update children
            if parent:
                parent.children[char] = node
        for char, child_node in list(node.children.items()):
            self.compress_trie(child_node, node, char)
        node.is_end_of_word = True

    def construct_suffix_tree_from_text(self, keys: list[str]):
        for word in keys:
            for i in range(len(word)):
                suffix = word[i:]
                current_node = self.root
                for char in suffix:
                    if char not in current_node.children:
                        current_node.children[char] = TrieNode(char)
                    current_node = current_node.children[char]
                current_node.is_end_of_word = True
        if self.is_compressed:
            self.compress_suffix(self.root)


    def compress_suffix(self, node: TrieNode, parent=None, char=None):
        while len(node.children) == 1 and not node.is_end_of_word:
            next_char, next_node = next(iter(node.children.items()))
            if len(next_node.children) == 1 and not next_node.is_end_of_word:
                # Merge the labels
                node.value += next_node.value
                node.is_end_of_word = next_node.is_end_of_word
                # Update parent's reference
                if parent:
                    parent.children[char] = node
                # Move to the next node
                node.children = next_node.children
            else:
                break
        for char, child_node in list(node.children.items()):
            self.compress_suffix(child_node, node, char)

    def search_and_get_depth(self, key):
        current_node = self.root
        depth = 0
        while key:
            if key[:len(current_node.value)] == current_node.value:
                depth += 1
                key = key[len(current_node.value):]
                if key:
                    current_node = current_node.children.get(key[0])
                    if not current_node:
                        return -1
            else:
                return -1
        return depth
