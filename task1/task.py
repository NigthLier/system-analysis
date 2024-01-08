import sys
import csv

def get_csv_data(file_name, row, col):
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        
        if row < len(data) and col < len(data[row]) and row >= 0 and col >= 0:
            return data[row][col]
        else:
            return 'Invalid row or column index'

def main():
    if len(sys.argv) != 4:
        print("Usage: python task.py <file_name> <row_index> <column_index>")
    else:
        file_name = sys.argv[1]
        row = int(sys.argv[2])
        col = int(sys.argv[3])
        print(get_csv_data(file_name, row, col))

if __name__ == "__main__":
    main()
