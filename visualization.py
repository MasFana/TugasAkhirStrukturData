class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.original_words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        lowercase_word = word.lower()
        node = self.root
        for char in lowercase_word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.original_words.append(word)

    def search(self, prefix):
        lowercase_prefix = prefix.lower()
        node = self.root
        traversal_path = []  # Track path for visualization
        for char in lowercase_prefix:
            traversal_path.append(char)
            if char not in node.children:
                print(f"Prefix not found: {' -> '.join(traversal_path)}")
                return []
            node = node.children[char]
        print(f"Traversal path for prefix '{prefix}': {' -> '.join(traversal_path)}")
        return self._autocomplete(node)

    def _autocomplete(self, node, prefix="", depth=0):
        print(f"{' ' * (2 * depth)}Autocomplete called at prefix '{prefix}'")
        suggestions = []
        if node.is_end_of_word:
            print(f"{' ' * (2 * depth)}Found: {node.original_words}")
            suggestions.extend(node.original_words)

        for char, child_node in node.children.items():
            suggestions.extend(self._autocomplete(child_node, prefix + char, depth + 1))
        return suggestions

    def print_trie(self, node=None, prefix=""):
        if node is None:
            node = self.root

        if node.is_end_of_word:
            print(f"{prefix} -> {node.original_words}")

        for char, child_node in node.children.items():
            self.print_trie(child_node, prefix + char)


# Example usage
books = [
    "Data Structures and Algorithms",
    "Database Management Systems",
    "Design Patterns"
]

trie = Trie()
for book in books:
    trie.insert(book)

print("Visualizing Trie:")
trie.print_trie()

print("\nSearching for prefix 'dat':")
results = trie.search("dat")
print("\nResults for 'dat':", results)
