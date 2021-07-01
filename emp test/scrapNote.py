print("\n")

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

COMBOS = []
DUPLICATES = []

for i in FLAVORS:

    for j in FLAVORS:

        if i != j or j != i:
            COMBOS.append(f"{i}, {j}")

# for i in COMBOS:
#     print(i)

# for i in COMBOS:
    # print('OG:', i)

# print(DUPLICATES)

c = 0
d = 0
for i in range(len(COMBOS)):
    while c < len(COMBOS):
        c += 6
        COMBOS.remove(COMBOS[c])
    while d < len(COMBOS):
        d += 11
        COMBOS.remove(COMBOS[d])

# 15 16 20 21 24 25 26 27 29 30 31 32

for i in range(len(COMBOS)):
    # print(i)
    # i += 1
    if i == 15 or i == 16 or i == 20 or i == 21 or i == 24 or i == 25:
        COMBOS.remove(COMBOS[i])

#


print(len(COMBOS))
for i in COMBOS:
    # print('updated:', i)
    print(i)
print("\n")

#
# Banana, Chocolate
# Banana, Lemon
# Banana, Pistachio
# Banana, Raspberry
# Banana, Strawberry
# Banana, Vanilla
# Chocolate, Lemon
# Chocolate, Pistachio
# Chocolate, Raspberry
# Chocolate, Strawberry
# Chocolate, Vanilla
# Lemon, Pistachio
# Lemon, Raspberry
# Lemon, Strawberry
# Lemon, Vanilla
# # Pistachio, Banana
# # Pistachio, Chocolate
# Pistachio, Raspberry
# Pistachio, Strawberry
# Pistachio, Vanilla
# # Raspberry, Banana
# # Raspberry, Chocolate
# Raspberry, Strawberry
# Raspberry, Vanilla
# # Strawberry, Banana
# # Strawberry, Chocolate
# # Strawberry, Lemon
# # Strawberry, Pistachio
# Strawberry, Vanilla
# # Vanilla, Banana
# # Vanilla, Chocolate
# # Vanilla, Lemon
# Vanilla, Pistachio
#
# Banana, Chocolate
# Banana, Lemon
# Banana, Pistachio
# Banana, Raspberry
# Banana, Strawberry
# Banana, Vanilla
# Chocolate, Lemon
# Chocolate, Pistachio
# Chocolate, Raspberry
# Chocolate, Strawberry
# Chocolate, Vanilla
# Lemon, Pistachio
# Lemon, Raspberry
# Lemon, Strawberry
# Lemon, Vanilla
# Pistachio, Chocolate
# Pistachio, Strawberry
# Pistachio, Vanilla
# Raspberry, Banana
# Raspberry, Chocolate
# Raspberry, Vanilla
# Strawberry, Chocolate
# Strawberry, Lemon
# Strawberry, Pistachio
# Vanilla, Banana
# Vanilla, Lemon
# Vanilla, Pistachio
