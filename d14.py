# --- Day 14: Chocolate Charts ---
# What are the scores of the ten recipes immediately after the number of recipes in your puzzle input?

# puzzle input
recipe_end = "598701"


def part_one():
    recipe = [3, 7]
    elf_1 = 0
    elf_2 = 1

    while len(recipe) < recipe_end + 10:
        elf_1_cook = recipe[elf_1]
        elf_2_cook = recipe[elf_2]
        score_sum = elf_1_cook + elf_2_cook
        for score_index in str(score_sum):
            recipe.append(int(score_index))

        elf_1 = (elf_1 + elf_1_cook + 1) % len(recipe)
        elf_2 = (elf_2 + elf_2_cook + 1) % len(recipe)

    result = "".join([str(x) for x in recipe[recipe_end: recipe_end + 10]])
    print(result)


def part_two():
    recipe = [3, 7]
    elf_1 = 0
    elf_2 = 1

    while True:
        elf_1_cook = recipe[elf_1]
        elf_2_cook = recipe[elf_2]
        score_sum = elf_1_cook + elf_2_cook
        for score_index in str(score_sum):
            recipe.append(int(score_index))

        elf_1 = (elf_1 + elf_1_cook + 1) % len(recipe)
        elf_2 = (elf_2 + elf_2_cook + 1) % len(recipe)

        # check if the recipe has ended
        ref_index = len(recipe) - len(recipe_end)
        first_try = "".join([str(x) for x in recipe[ref_index - 1: -1]])
        second_try = "".join([str(x) for x in recipe[ref_index:]])

        if first_try == recipe_end:
            result = ref_index - 1
            break
        elif second_try == recipe_end:
            result = ref_index
            break

    print(result)


part_two()
