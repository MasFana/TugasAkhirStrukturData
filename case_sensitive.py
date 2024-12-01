class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        word = word.lower()  # Konversi menjadi lowercase
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        prefix = prefix.lower()  # Konversi input pencarian menjadi lowercase
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._autocomplete(node, prefix)

    def _autocomplete(self, node, prefix):
        suggestions = []
        if node.is_end_of_word:
            suggestions.append(prefix)

        for char, child_node in node.children.items():
            suggestions.extend(self._autocomplete(child_node, prefix + char))
        return suggestions


# Daftar nama buku perpustakaan
books = [
    "Data Structures and Algorithms",
    "Database Management Systems",
    "Design Patterns",
    "Deep Learning for Natural Language Processing",
    "Distributed Systems",
    "Discrete Mathematics",
    "Digital Signal Processing"
]

# Inisialisasi Trie
trie = Trie()
for book in books:
    trie.insert(book)

# Input pencarian dari pengguna
query = 'dat'

# Hasil pencarian
results = trie.search(query)
if results:
    print("Hasil pencarian yang mirip:")
    for book in results:
        print(f"- {book}")
else:
    print("Tidak ditemukan nama buku yang cocok.")
