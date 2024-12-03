# Inisialisasi Trie
from Trie import Trie, TrieNode, Data, Clear, print_table

# Inisialisasi Trie dan HashMap
data = Data()
buku = data.get_data()
trie = Trie()


# Struktur Buku : {'Kode Buku': {'Judul', 'Penulis', 'Tahun-Publikasi', 'Penerbit', 'Url}  }
for key, value in buku.items():
    # Memasukkan Judul dan Key Buku ke Trie
    trie.insert(value['Judul'], key)
    
while True:
    Clear()
    print(r"""
  _____                 _          _         _                                  _      _       
 |  ___|_ _ _ __   __ _( )___     / \  _   _| |_ ___   ___ ___  _ __ ___  _ __ | | ___| |_ ___ 
 | |_ / _` | '_ \ / _` |// __|   / _ \| | | | __/ _ \ / __/ _ \| '_ ` _ \| '_ \| |/ _ \ __/ _ \
 |  _| (_| | | | | (_| | \__ \  / ___ \ |_| | || (_) | (_| (_) | | | | | | |_) | |  __/ ||  __/
 |_|  \__,_|_| |_|\__,_| |___/ /_/   \_\__,_|\__\___/ \___\___/|_| |_| |_| .__/|_|\___|\__\___|
                                                                         |_|                   

          """)
    
    keyword = input("Masukkan kata kunci : ")
    suggestions = trie.search(keyword)
    
    # print(suggestions)
    
    print_table([buku[i[0]] for i in suggestions])
    
    # for i in suggestions:
    #     print(buku[i[0]])
    
    input("\nTekan Enter untuk melanjutkan...")