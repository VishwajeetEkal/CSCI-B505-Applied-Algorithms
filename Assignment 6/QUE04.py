def maximumPeople(personHeight, roomHeight):
    personHeight.sort()  

    maxPeople = 0
    itrPeople, itrRoom = 0, 0
    run =len(roomHeight)
    while itrPeople < len(personHeight) and itrRoom < run:
        if personHeight[itrPeople] <= roomHeight[itrRoom]:
            itrRoom+=1            
        elif itrRoom -1 >=0 :
            maxPeople +=1
            run = itrRoom-1
            itrPeople+=1
            itrRoom=0
            continue
        else:
            return maxPeople
            
        if itrRoom == run and itrPeople < len(personHeight):
            maxPeople +=1
            run = itrRoom-1
            itrPeople+=1
            itrRoom=0
            
    return maxPeople




print(maximumPeople([ 2, 2, 5, 5 ], [ 6, 1, 1, 2, 3, 4, 3, 7, 5, 6, 2, 8, 8, 5 ]))  
print(maximumPeople([1, 1, 1,1], [2, 2, 2]))  # Output: 3
print(maximumPeople([4, 1, 8, 7], [7, 4, 2, 2, 5]))  # Output: 3
print(maximumPeople([2, 4, 5, 6], [2, 3, 3, 3, 6, 7]))  # Output: 1
print(maximumPeople([1, 3, 6, 8, 12, 14, 18, 20, 22, 24, 26, 29, 31, 32, 32, 33, 33],
                    [1, 4, 5, 6, 8, 9, 12, 12, 12, 13, 15, 16, 19, 20, 22, 24, 27, 28, 30, 32]))  # Output: 4
print(maximumPeople([2, 2, 5, 5], [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8]))  # Output: 1