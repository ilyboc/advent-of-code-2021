inp = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''
from collections import defaultdict
inp = list(inp.split("\n"))
polymer = defaultdict(lambda: 0)
elements = defaultdict(lambda: 0)
for i in range(len(inp[0])):
    if i+1 < len(inp[0]): polymer[inp[0][i:i+2]] += 1
    elements[inp[0][i]] += 1
pairs = defaultdict(lambda: None)
for i in range(2, len(inp)):
    pairs[inp[i].split(" -> ")[0]] = inp[i].split(" -> ")[1]
print(elements)
for step in range(10):
    print ("Step:", step)
    polymer_temp = polymer.copy()
    for key in list(polymer_temp.keys()):
        if pairs[key] is not None and polymer_temp[key] > 0:
            polymer[key[0] + pairs[key]] += polymer_temp[key]
            polymer[pairs[key] + key[1]] += polymer_temp[key]
            elements[pairs[key]] += polymer_temp[key]
            polymer[key] -= polymer_temp[key]
    print(elements)
sorted_elements = sorted(elements.values())
print (sorted_elements[-1]-sorted_elements[0]) 