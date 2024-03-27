from trie import Trie
data = ["test", "toaster", "toasting", "slow", "slowly"]
uncompressed_trie = Trie(is_compressed=False)
uncompressed_trie.construct_trie_from_text(data)
uncompressed_trie.print_trie()

compressed_trie = Trie(is_compressed=True)
compressed_trie.construct_trie_from_text(data)
compressed_trie.print_trie()