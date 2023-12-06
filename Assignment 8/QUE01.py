import copy


def translate_message(arr):
    
    arr = copy.deepcopy(arr)

    arr.sort()

    indices = {}

    
    result = 0

    
    for x in arr:
    
        result = 0

        if x - 7 in indices:
    
            result = max(result, indices[x - 7] + 1)

    
        if x + 7 in indices:
    
            result = max(result, indices[x + 7] + 1)

        indices[x] = result
    
    return max(indices.values())+1

# Examples
arr1 = [1,
        8,
        15,
        23,
        29,
        36,
        43]
print(translate_message(arr1))  # Output: 2

arr1 = [2, 9, 1]
print(translate_message(arr1)) 

arr2 = [6, 0, 14, 4, 7, 3]
print(translate_message(arr2))  # Output: 3
