import sys
import csv

def get_csv_graph(csv_file):
    matrix = {}
    
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            node1, node2 = row
            
            if node1 not in matrix:
                matrix[node1] = []
            if node2 not in matrix:
                matrix[node2] = []
            
            matrix[node1].append(node2)
            matrix[node2].append(node1)
    
    return matrix

def print_graph(matrix):
    for node, neighbors in matrix.items():
        print(f"{node}: {neighbors}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Task1.py <file_name>")
    else:
        file_name = sys.argv[1]
        matrix = get_csv_graph(file_name)
        print_graph(matrix)


if __name__ == "__main__":
    main()
