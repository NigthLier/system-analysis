import json
import sys
import numpy as np

def task(a_data, b_data):
    def calc_table(data, mapping=None):
        if mapping is None:
            mapping = {i: e for i, e in enumerate(el for cl in data for el in (cl if isinstance(cl, list) else [cl]))}
        
        a = {e: i for i, cl in enumerate(data) for e in (cl if isinstance(cl, list) else [cl])}
                    
        length = len(mapping)
        table = np.zeros((length, length))

        for i in range(length):
            for j in range(length):
                if a[mapping[j]] <= a[mapping[i]]:
                    table[j,i] = 1

        return table, mapping
    
    a, mapping = calc_table(a_data, None)
    b, mapping = calc_table(b_data, mapping)
    
    a, b = np.array(a), np.array(b)
    a_b, a_b_t = np.logical_and(a, b), np.logical_and(a.T, b.T)

    zeros = {(i, j) for i in range(len(a)) for j in range(len(a)) if not (a_b[i, j] or a_b_t[i, j])}
    zeros = [[mapping[i], mapping[j]] for i, j in zeros]

    merged = []
    for pair in zeros:
        for mr in merged:
            if set(pair) & set(mr):
                mr.update(pair)
                break
        else:
            merged.append(set(pair))

    controversy = [list(set(i)) for i in merged]
    answer, visited = [], set()

    for val in mapping.values():
        if val not in visited:
            cl = {val}
            visited.add(val)

            for con in controversy:
                if val in con:
                    cl.update(con)
                    visited.update(con)

            answer.append(list(cl) if len(cl) > 1 else cl.pop())
    
    return answer

def main():
    if len(sys.argv) != 3:
        print("Usage: python task.py <json string> <json string>")
    else:
        json_string1 = json.loads(sys.argv[1])
        json_string2 = json.loads(sys.argv[2])
        result_json = task(json_string1, json_string2)
        print(result_json)

if __name__ == "__main__":
    main()

