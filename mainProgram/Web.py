# Inisialisasi Trie
from Trie import Trie, Data
from flask import Flask, jsonify,render_template

app = Flask(__name__)

# Inisialisasi Trie dan HashMap
data = Data()
buku = data.get_data()
trie = Trie()


# Struktur Buku : {'Kode Buku': {'Judul', 'Penulis', 'Tahun-Publikasi', 'Penerbit', 'Url}  }
for key, value in buku.items():
    # Memasukkan Judul dan Key Buku ke Trie
    trie.insert(value['Judul'], key)
    

@app.route('/search/<nama>', methods=['GET'])
def search(nama):
    print(nama)
    if not nama:
        return jsonify({'error': 'Query parameter is required'}), 400
    
    results = trie.search(nama)
    if not results:
        return jsonify({'message': 'No results found'}), 404
    results = [buku[i[0]] for i in results[:10]]
    return jsonify({'results': results})
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=6969)