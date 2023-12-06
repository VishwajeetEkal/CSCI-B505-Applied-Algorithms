def aliveOrDead(trees, tigersWish):
    numericTreeIndices = {}

    for itr, tree in enumerate(trees):
        if tree != 'X':
            value = int(tree)
            if value not in numericTreeIndices:
                numericTreeIndices[value] = []
            numericTreeIndices[value].append(itr)

    uniqueValues = list(numericTreeIndices.keys())
    for i in range(len(uniqueValues) - 1):
        for j in range(i + 1, len(uniqueValues)):
            valueOne, valueTwo = uniqueValues[i], uniqueValues[j]
            target_value = tigersWish - (valueOne + valueTwo)
            print
            if target_value in uniqueValues:
                return 'Alive'
    return 'Dead'

    
    return 'Dead'



trees1 = ['2', 'X', '7', '4', 'X', '-1', '10', 'X', 'X']
tigersWish1 = 18
print(aliveOrDead(trees1, tigersWish1))  # Output: 'Alive'

trees2 = ['X', 'X', 'X', '1']
tigersWish2 = 8
print(aliveOrDead([
        "2",
        "X",
        "7",
        "-1",
        "X",
        "5",
        "10",
        "X",
        "X"
    ],
    18))  # Output: 'Dead'
