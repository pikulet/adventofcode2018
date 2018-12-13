# --- Day 10: The Stars Align ---
# What message will eventually appear in the sky?

# Solution is incomplete due to problems with scaling pyplot.

import re
import matplotlib.pyplot as plt

with open('d10-input.txt', 'r') as f:
    data = f.readlines()

parsed_data = list()
for d in data:
    d = re.split("<|,|>", d)
    position = [int(d[1]), int(d[2][1:])]
    velocity = int(d[4]), int(d[5][1:])
    parsed_data.append((position, velocity))


def pass_time():
    for p, v in parsed_data:
        p[0] += v[0]
        p[1] += v[1]


def print_stars():
    for p, v in parsed_data:
        plt.scatter(p[0], p[1])
    plt.show()


for i in range(100000):
    pass_time()
    if i % 200 == 0:
        print_stars()
