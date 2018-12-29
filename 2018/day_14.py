
def get_new_recipe(total):
    new_recipe = [int(s) for s in str(total)]
    return new_recipe

assert get_new_recipe(10) == [1, 0]
assert get_new_recipe(1) == [1]

def make_recipe(num_recipes):
    scores = [3, 7]
    elf_1 = 0
    elf_2 = 1
    while len(scores) < num_recipes:
        new_recipe = get_new_recipe(scores[elf_1] + scores[elf_2])
        scores.extend(new_recipe)
        elf_1 = (elf_1 + scores[elf_1] + 1) % len(scores)
        elf_2 = (elf_2 + scores[elf_2] + 1) % len(scores)
    return scores

print (make_recipe(20))
if __name__ == "__main__":
    n = 323081
    scores = make_recipe(n + 10)
    ten_after = [str(x) for x in scores[n:n+10]]
    print(''.join(ten_after))
    # scores = make_recipe(n)
