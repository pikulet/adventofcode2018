# --- Day 5: Alchemical Reduction ---
# How many units remain after fully reacting the polymer you scanned?
from functools import reduce

with open('d05-input.txt', 'r') as f:
    data = f.read()


reaction_reference = dict(zip(list(range(len(data))), [1]*len(data)))


def react_unit(u, polymer):
    # check if unit is reacted
    if polymer[u] == 0 or u == len(data) - 1:
        return False

    # find next unreacted unit
    i = 1
    while polymer[u+i] == 0:
        i += 1
        if u + i >= len(data):
            return False

    # check if a reaction occurs
    if abs(ord(data[u]) - ord(data[u+i])) == 32:
        polymer.update({u: 0})
        polymer.update({u + i: 0})
        return True

    return False


def react(polymer):
    reaction_occurred = True
    while reaction_occurred:
        reaction_occurred = reduce(lambda x, y: x or y, [react_unit(i, polymer) for i in range(len(polymer))])

    return len(list(filter(lambda x: x == 1, polymer.values())))


result = react(reaction_reference)
print(result)


result = len(data)
for letter in range(26):
    copy = reaction_reference.copy()
    for i in range(len(data)):
        if ord(data[i]) == 65 + letter or ord(data[i]) == 97 + letter:
            copy.update({i: 0})
    result = min(result, react(copy))

print(result)
