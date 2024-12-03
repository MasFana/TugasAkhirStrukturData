import os
import tabulate
import csv

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.key = []  # Menyimpan kata dalam case aslinya

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word,key):
        lowercase_word = word.lower()  # Konversi menjadi lowercase untuk penyimpanan di Trie
        node = self.root
        for char in lowercase_word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.key.append([key])  # Simpan versi asli kata

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
            suggestions.extend(node.key)  # Ambil semua key dari simpul ini

        for char, child_node in node.children.items():
            suggestions.extend(self._autocomplete(node=child_node))
        return suggestions

class Data:
    def __init__(self):
        self.data = {}
        self.read_data()
    
    def read_data(self):
        with open('buku.csv', 'r') as file:
            reader = csv.reader(file,delimiter=';')
            data = list(reader)
            
        header = data.pop(0)[1:]
        print(header)
        for i in data:
            try:
                key = i.pop(0)
                self.data[key] = {}
                for h in range(len(header)):
                    self.data[key][header[h]] = i[h]
            except:
                print(i)
                return
                
    def get_data(self):
        return self.data

def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_table(data):
    print(tabulate.tabulate(data, headers='keys', tablefmt='fancy_grid'))
