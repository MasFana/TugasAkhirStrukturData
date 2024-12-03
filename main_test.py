import csv 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.original_words = []  # Menyimpan kata dalam case aslinya

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        lowercase_word = word.lower()  # Konversi menjadi lowercase untuk penyimpanan di Trie
        node = self.root
        for char in lowercase_word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.original_words.append(word)  # Simpan versi asli kata

    def search(self, prefix):
        lowercase_prefix = prefix.lower()  # Konversi prefix menjadi lowercase
        node = self.root
        for char in lowercase_prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._autocomplete(node)

    def _autocomplete(self, node):
        suggestions = []
        if node.is_end_of_word:
            suggestions.extend(node.original_words)  # Ambil semua kata asli dari simpul ini

        for char, child_node in node.children.items():
            print(char)
            suggestions.extend(self._autocomplete(child_node))
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
query = input("Masukkan kata pencarian: ").strip()

# Hasil pencarian
results = trie.search(query)
if results:
    print("Hasil pencarian yang mirip:")
    for book in results:
        print(f"- {book}")
else:
    print("Tidak ditemukan nama buku yang cocok.")




