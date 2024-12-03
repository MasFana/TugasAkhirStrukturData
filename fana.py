import csv
import tabulate

def read_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f,delimiter=';')
        data = list(reader)
    return data

def write_csv(file, data):
    with open(file, 'w',newline='') as f:
        writer = csv.writer(f,delimiter=';')
        writer.writerows(data)
    
def print_table(data):
    print(tabulate.tabulate(data, headers='firstrow', tablefmt='rounded_outline'))

def remove_column(data, col_index):
    for row in data:
        del row[col_index]
    return data

a = read_csv('books_modified.csv')

print_table(a[:100])