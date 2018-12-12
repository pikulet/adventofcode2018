# --- Day 12: Subterranean Sustainability ---
# After 20 generations, what is the sum of the numbers of all pots which contain a plant?

with open('d12-input.txt', 'r') as f:
    data = f.readlines()

empty_symbol = "."
full_symbol = "#"


def parse_initial_state(initial_state_string):
    initial_state_string = initial_state_string[len("initial state: "): len(initial_state_string) - 1]
    state = dict()

    for i in range(len(initial_state_string)):
        state.setdefault(i, initial_state_string[i])

    return state


def parse_rules(rules):
    return dict(zip([rule[:5] for rule in rules], [rule[-2] for rule in rules]))


state = parse_initial_state(data[0])
rules = parse_rules(data[2:])


# find the sequence of 5 pots to the left and right of [index]
def get_pots(index):
    left_1 = state.get(index - 2) or empty_symbol
    left_2 = state.get(index - 1) or empty_symbol
    val = state.get(index)
    right_1 = state.get(index + 1) or empty_symbol
    right_2 = state.get(index + 2) or empty_symbol
    pot_line = left_1 + left_2 + val + right_1 + right_2
    return pot_line


def process_generation():
    new_state = dict()

    for pot_index in state:
        pot_line = get_pots(pot_index)
        new_pot_state = rules.get(pot_line)
        new_state.setdefault(pot_index, new_pot_state)

    return new_state


# create at least three empty pots at the left and right edges
def fill_pots():
    global state
    filled_pots = sorted(filter(lambda x: state.get(x) == full_symbol, state.keys()))

    min_pot_filled = filled_pots[0]
    min_state = min(state)
    num_pots_to_add_left = 3 - (min_pot_filled - min_state)

    if 0 < num_pots_to_add_left <= 3:
        for p in range(num_pots_to_add_left):
            state.setdefault(min_state - 1 - p, empty_symbol)

    max_pot_filled = filled_pots[-1]
    max_state = max(state)
    num_pots_to_add_right = 3 - (max_state - max_pot_filled)
    if 0 < num_pots_to_add_right <= 3:
        for p in range(num_pots_to_add_right):
            state.setdefault(max_state + 1 + p, empty_symbol)


def find_sum():
    sum = 0
    for index, pot in state.items():
        if pot == full_symbol:
            sum += index
    return sum


previous_sum = 0
previous_difference = -1
fifty_billion = 50000000000

for generation in range(fifty_billion):
    fill_pots()
    state = process_generation()
    result = find_sum()

    if generation == 20:
        print("Generation 20 :", result)

    difference = result - previous_sum
    if difference == previous_difference:
        # search for the converging generation
        print("Generation :", generation, ", Current result :", result, ", Difference :", difference)
        break

    previous_sum = result
    previous_difference = difference

# add 1 as generation starts from 0 instead of 1
result += (fifty_billion - (generation + 1)) * difference
print(result)

