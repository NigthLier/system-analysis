import csv
from io import StringIO

def calculate_extensional_lengths(csv_string):
    reader = csv.reader(StringIO(csv_string))

    matrix = {}
    
    for row in reader:
        node1, node2 = row
        
        if node1 not in matrix:
            matrix[node1] = []
        if node2 not in matrix:
            matrix[node2] = []
            
        matrix[node1].append(node2)
    
    matrix = dict(sorted(matrix.items()))
    
    
    result = {}
    
    for node in matrix:
        result[node] = {"r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0}
    
    
    def rec(node):
        i = 1
        for n in matrix[node]:
            result[n]["r4"] += 1
            i += rec(n)
        return i

    for node in matrix:
        result[node]["r1"] += len(matrix[node])
        for n in matrix[node]:
            result[n]["r2"] += 1
            result[n]["r5"] += len(matrix[node]) - 1
        result[node]["r3"] = rec(node) - result[node]["r1"] - 1
        result[node]["r4"] -= result[node]["r2"]
    
    
    output = StringIO()
    writer = csv.writer(output)
    for node, lengths in result.items():
        writer.writerow([lengths["r1"], lengths["r2"], lengths["r3"], lengths["r4"], lengths["r5"]])
    
    return output.getvalue()



def main():
    csv_string = "1,2\n2,3\n2,6\n3,4\n3,5"
    result_csv = calculate_extensional_lengths(csv_string)
    print(result_csv)


if __name__ == "__main__":
    main()