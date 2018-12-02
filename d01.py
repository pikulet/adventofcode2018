# After feeling like you've been falling for a few minutes, you look at the
# device's tiny screen. "Error: Device must be calibrated before first use.
# Frequency drift detected. Cannot maintain destination lock." Below the
# message, the device shows a sequence of changes in frequency (your puzzle
# input). A value like +6 means the current frequency increases by 6; a value
#  like -3 means the current frequency decreases by 3.
# For example, if the device displays frequency changes of +1, -2, +3, +1,
# then starting from a frequency of zero, the following changes would occur:
#
# Current frequency  0, change of +1; resulting frequency  1.
# Current frequency  1, change of -2; resulting frequency -1.
# Current frequency -1, change of +3; resulting frequency  2.
# Current frequency  2, change of +1; resulting frequency  3.
# In this example, the resulting frequency is 3.
#
# Here are other example situations:
#
# +1, +1, +1 results in  3
# +1, +1, -2 results in  0
# -1, -2, -3 results in -6
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

