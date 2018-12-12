# --- Day 2: Inventory Management System ---
# What is the checksum for your list of box IDs?

f = open('d02-input.txt', 'r')
data = f.readlines()


def find_checksum():
    two_repeats = 0
    three_repeats = 0

    for box_id in data:
        box_id = list(box_id)

        def count_char(char):
            return box_id.count(char)

        count = list(map(count_char, box_id))
        if 2 in count:
            two_repeats += 1
        if 3 in count:
            three_repeats += 1

    return two_repeats * three_repeats


print("Checksum :", find_checksum())

# --- Part Two ---
# What letters are common between the two correct box IDs?


def difference_count(id_1, id_2):
    diff = 0
    for i in range(len(id_1)):
        if id_1[i] != id_2[i]:

            # short circuit break when difference is more than 1
            if diff == 1:
                return -1

            diff += 1

    return diff


def remove_diff_letter(id_1, id_2):
    for i in range(len(id_1)):
        if id_1[i] != id_2[i]:
            return id_1[:i] + id_1[i+1:]


def find_correct_boxes():
    for box_id_1 in data:
        for box_id_2 in data:
            if difference_count(box_id_1, box_id_2) == 1:
                return remove_diff_letter(box_id_1, box_id_2)


print("Correct box ID :", find_correct_boxes())