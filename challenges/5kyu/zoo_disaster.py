rules = """antelope eats grass
big-fish eats little-fish
bug eats leaves
bear eats big-fish
bear eats bug
bear eats chicken
bear eats cow
bear eats leaves
bear eats sheep
chicken eats bug
cow eats grass
fox eats chicken
fox eats sheep
giraffe eats leaves
lion eats antelope
lion eats cow
panda eats leaves
sheep eats grass
"""

def get_zoo():
    zoo = {}
    for r in rules.splitlines():
        a1, v, a2 = r.split(" ")
        if a1 in zoo:
            zoo[a1].append(a2)
        else:
            zoo[a1] = [a2]
    return zoo
# print get_zoo()

def who_eats_who(zoo):
    animals = zoo.split(",")
    result = [zoo]
    zoo_rules = get_zoo()
    i, j = 0, 1
    count = len(animals)
    while count > 1 and i < count:
        a, c = animals[i], animals[j]
        options = zoo_rules.get(a, [])
        if c in options:
            del animals[j]
            result.append("{0} eats {1}".format(a, c))
            count -= 1
            i, j = 0, 1
        elif options and (j == i - 1 and i < count - 1):
            j = i + 1
        else:
            j, i = i, i+1
    return result + [",".join(animals)]


input_str = "fox,bug,chicken,grass,sheep"
expected = ["fox,bug,chicken,grass,sheep",
            "chicken eats bug",
            "fox eats chicken",
            "sheep eats grass",
            "fox eats sheep",
            "fox"]
result = who_eats_who(input_str)
print result
assert result == expected

input_str = 'grass,grass,cow,leaves,bug,big-fish,leaves,bear'
expected = [
    'grass,grass,cow,leaves,bug,big-fish,leaves,bear',
    'cow eats grass',
    'cow eats grass',
    'bug eats leaves',
    'bear eats leaves', 'bear eats big-fish', 'bear eats bug', 'bear eats cow', 'bear']
result = who_eats_who(input_str)
print result[1:]
assert result == expected

input_str = 'big-fish,bug,banana,chicken,chicken,leaves,chicken,fox,bug,busker,grass,fox,little-fish'
expected = [
    'big-fish,bug,banana,chicken,chicken,leaves,chicken,fox,bug,busker,grass,fox,little-fish',
    'fox eats chicken',
    'big-fish,bug,banana,chicken,chicken,leaves,fox,bug,busker,grass,fox,little-fish']
result = who_eats_who(input_str)
print result[1:]
assert result == expected
