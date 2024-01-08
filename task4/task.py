import math
from collections import Counter

def task():
    outcomes = [(i, j) for i in range(1, 7) for j in range(1, 7)]

    sums = Counter(a+b for a, b in outcomes)
    products = Counter(a*b for a, b in outcomes)
    
    total_outcomes = len(outcomes)
    prob_sums = {k: v / total_outcomes for k, v in sums.items()}
    prob_products = {k: v / total_outcomes for k, v in products.items()}

    joint_probs = Counter((a+b, a*b) for a, b in outcomes)
    prob_joint = {k: v / total_outcomes for k, v in joint_probs.items()}

    H_A = -sum(p * math.log2(p) for p in prob_sums.values())
    H_B = -sum(p * math.log2(p) for p in prob_products.values())
    H_AB = -sum(p * math.log2(p) for p in prob_joint.values())
    HA_B = H_AB - H_A
    I_AB = H_A + H_B - H_AB

    return [round(H_AB, 2), round(H_A, 2), round(H_B, 2), round(HA_B, 2), round(I_AB, 2)]

def main():
    result = task()
    print(result)

if __name__ == "__main__":
    main()