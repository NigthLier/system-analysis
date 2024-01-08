import json
import sys
import numpy as np

def task(a_data, b_data):
    mapping, places = {e: i for i, cl in enumerate(a_data, 1) for e in (cl if isinstance(cl, list) else [cl])}, []

    for mark in [a_data, b_data]:
        row = [mapping[e] for el in mark for e in (el if isinstance(el, list) else [el])]
        places.append(row)
        
    x_max = np.arange(1, len(places[0]) + 1) * len(places)
    d_max = np.sum((x_max - np.mean(x_max))**2) / (len(places[0]) - 1)

    x = np.sum(np.array(places).T, axis=1)
    d = np.sum((x - np.mean(x_max))**2) / (len(places[0]) - 1)
    return round(d / d_max, 2)

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
