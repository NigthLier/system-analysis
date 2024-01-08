import csv
import sys
import math
from io import StringIO

def task(csv_string):
  reader = csv.reader(StringIO(csv_string))
  matrix = list(reader)
  length = len(matrix)
  
  entropy = 0
  for row in matrix:
    for cell in row:
        if cell != '0':
            d = float(cell) / (length - 1)
            entropy -= d * math.log2(d)
      
  return round(entropy, 1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python task.py <csv string>")
    else:
        csv_string = sys.argv[1]
        csv_string = csv_string.replace('\\n', '\n')
        result_csv = task(csv_string)
        print(result_csv)

if __name__ == "__main__":
    main()