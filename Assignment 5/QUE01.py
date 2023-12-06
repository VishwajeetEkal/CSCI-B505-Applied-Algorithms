def busRemaining(busStation) :
    if len(busStation)==0:
        return 1
    
    busRemain = len(busStation)
    max = busStation[0][1]
    for i in range(1,len(busStation)):
        if max >= busStation[i][0]:
            busRemain-=1
            if max < busStation[i][1]:
                max = busStation[i][1]
        else:
            max = busStation[i][1]

    return busRemain


print(busRemaining([[2,8], [6, 10], [12, 14], [12, 20]]))
print(busRemaining([[1,4],[2,5],[3,6],[7,10],[8,9],[11,15],[12,14],[16,20],[17,18],[19,20]]))
print(busRemaining([]))
