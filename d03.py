# --- Day 3: No Matter How You Slice It ---
# The Elves managed to locate the chimney-squeeze prototype fabric for
# Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall
#  of the warehouse in the middle of the night). Unfortunately, anomalies are
#  still affecting them - nobody can even agree on how to cut the fabric.
#
# The whole piece of fabric they're working on is a very large square - at
# least 1000 inches on each side.
#
# Each Elf has made a claim about which area of fabric would be ideal for
# Santa's suit. All claims have an ID and consist of a single rectangle with
# edges parallel to the edges of the fabric. Each claim's rectangle is
# defined as follows:
#
# The number of inches between the left edge of the fabric and the left edge
# of the rectangle.
# The number of inches between the top edge of the fabric and the top edge of
#  the rectangle.
# The width of the rectangle in inches.
# The height of the rectangle in inches.
# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle
# 3 inches from the left edge, 2 inches from the top edge, 5 inches wide,
# and 4 inches tall.
#
# The problem is that many of the claims overlap, causing two or more claims
# to cover part of the same areas. For example, consider the following claims:
#
# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2

# If the Elves all proceed with their own plans, none of them will have
# enough fabric. How many square inches of fabric are within two or more claims?

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
# Amidst the chaos, you notice that exactly one claim doesn't overlap by even
#  a single square inch of fabric with any other claim. If you can somehow
# draw attention to it, maybe the Elves will be able to make Santa's suit after
# all!
#
# For example, in the claims above, only claim 3 is intact after all claims are
# made.
# 
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
