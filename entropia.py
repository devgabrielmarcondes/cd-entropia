from math import log2

classes = int(input("How many classes: "))

def entropy(classes):
    sumc = 0
    for p in range(0, classes):
        p = float(input(f"Probability: "))

        if classes > 1 and (p <= 0 or p >= 1):
            raise Exception("Invalid probability.")
        
        sumc += -p * log2(p)
    return sumc

def maxEntropy(classes):
    maxResult = log2(classes)
    return maxResult

print(f"\nThe entropy is: {entropy(classes)}\nThe max entropy is: {maxEntropy(classes)}")


