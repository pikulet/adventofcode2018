# --- Day 3: No Matter How You Slice It ---
# How many square inches of fabric are within two or more claims?

f = open('d03-input.txt', 'r')
data = f.readlines()


def parse_claim(claim):
    claim = claim.split()
    claim_id = parse_id(claim[0])
    claim_position = parse_position(claim[2])
    claim_dimension = parse_dimension(claim[3])
    return claim_id, claim_position, claim_dimension


def parse_id(id_format):
    return int(id_format[1:])


def parse_position(position_format):
    position_format = position_format.split(",")
    left = int(position_format[0])
    top = int(position_format[1][:-1])
    return left, top


def parse_dimension(dimension_format):
    dimension_format = dimension_format.split("x")
    width = int(dimension_format[0])
    height = int(dimension_format[1])
    return width, height


# claims made on the fabric can be found with fabric[row][column]
fabric = dict()


def fill_fabric():
    for claim in data:
        claim = parse_claim(claim)
        process_claim(claim)


def process_claim(claim):
    global fabric

    claim_id = claim[0]
    position_left = claim[1][0]
    position_top = claim[1][1]
    dimension_width = claim[2][0]
    dimension_height = claim[2][1]

    for h in range(dimension_height):
        row = position_top + h
        fabric.setdefault(row, dict())
        for w in range(dimension_width):
            column = position_left + w
            fabric.get(row).setdefault(column, set())
            fabric.get(row).get(column).add(claim_id)


def check_overlap_fabric():
    overlap = 0

    for row in fabric.values():
        for entry in row.values():
            if len(entry) > 1:
                overlap += 1

    return overlap


fill_fabric()
print("Overlap fabric area :", check_overlap_fabric())

# --- Part Two ---
# What is the ID of the only claim that doesn't overlap?


def find_no_overlap_claim():
    overlapping_claims = set()
    solo_claims = set()

    for row in fabric.values():
        for entry in row.values():
            if len(entry) > 1:
                overlapping_claims = overlapping_claims.union(entry)
            elif len(entry) == 1:
                solo_claims.add(list(entry)[0])

    solo_claims = solo_claims.difference(overlapping_claims)
    return list(solo_claims)[0]


print("Non-overlapping claim :", find_no_overlap_claim())
