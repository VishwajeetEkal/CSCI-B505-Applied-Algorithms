def solution_inheritance(num_items, num_boxes, children):
    if children > num_boxes or children == 0:
        return -1

    low, high = max(num_items), sum(num_items)

    while low < high:
        mid = (low + high) // 2
        dvde = 1  # Initialize the division count
        csum = 0  # Initialize the running sum
        max_item = 0  # Initialize the maximum value in the current division

        for num in num_items:
            if csum + num > mid:
                dvde += 1
                csum = 0
                max_item = 0

            csum += num
            max_item = max(max_item, num)

        if dvde <= children and max_item <= mid:
            high = mid
        else:
            low = mid + 1

    return low

print(solution_inheritance([15,17,14,19,14,13],6,0))
print(solution_inheritance([1,5,3,4,8,7,6,2],8,5))