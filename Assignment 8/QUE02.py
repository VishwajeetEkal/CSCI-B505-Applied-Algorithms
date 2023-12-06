def find_order_size(orders):
    
    unique_shields = set()

    
    symmetric_pairs = 0

    
    for order in orders:
        print(unique_shields)
        
        [a,b] = order
        
    
        if (b,a) in unique_shields:
            unique_shields.remove((b,a))
            unique_shields.add((a,b))
            symmetric_pairs +=1 
        else:
            unique_shields.add((a,b))

    
    order_size = len(orders) - symmetric_pairs

    return order_size

orders1 = [[1, 2], [2, 1]]
print(find_order_size(orders1))  # Output: 1

orders2 = [[5, 8], [3, 2], [5, 8]]
print(find_order_size(orders2))



orders3 = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5], [10, 5]]
print(find_order_size(orders3))  # Output: 3

