# --- Day 1: Chronal Calibration ---
# Starting with a frequency of zero, what is the resulting frequency after
# all of the changes in frequency have been applied?

f = open('d01-input.txt', 'r')
data = f.readlines()

# frequency and set of frequencies encountered before
frequency = 0
f_set = set([frequency])

plus = "+"
minus = "-"


# Part 1a processing input data
def process_freq_change(f_change):
    global frequency
    op = f_change[0]
    val = int(f_change[1:])

    # adjust frequency
    if op == plus:
        frequency += val
    elif op == minus:
        frequency -= val


for f_change in data:
    process_freq_change(f_change)
    
print("Final frequency :", frequency)

# --- Part Two ---
# What is the first frequency your device reaches twice?


# Part 1b
def find_repeated_freq():

    global frequency
    frequency = 0

    while True:
        for f_change in data:
            process_freq_change(f_change)
    
            # checking for repeated frequencies
            if frequency in f_set:
                return frequency
            else:
                f_set.add(frequency)


print("First repeated frequency :", find_repeated_freq())

