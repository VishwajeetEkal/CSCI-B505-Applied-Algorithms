def is_movePossible(x,y,i,j):
    if x ==i and y==j:
        return True
    elif x > i or y >j:
        return False
    
    x_move = is_movePossible(x+y,y,i,j)

    y_move = is_movePossible(x,x+y,i,j)

    return x_move or y_move

def count_successful_school_commutes(home_coords, school_coords, N):
    result = 0
    for h,s in zip(home_coords, school_coords):
        x ,y = h[0], h[1]
        i ,j = s[0], s[1]
        if is_movePossible(x,y,i,j):
            result += 1
    return result


print(count_successful_school_commutes(home_coords = [[1,1],[2,4]], school_coords = [[4,5],[2,5]], N=2))
print(count_successful_school_commutes(home_coords = [[3,2],[1,1],[4,4]], school_coords = [[8,5],[4,5],[7,7]], N=3))