def MaximumDeafPeople(Coordinates):
    def findMaxDeaf(itrPepShout,visited):
        visited.append(itrPepShout)
        deafCount = 1  

        itr = 0
        while itr < len(Coordinates):
            if itr not in visited and withinAudibleRange(itrPepShout, itr):
                visited.append(itr)
                deafCount += findMaxDeaf(itr, visited)
            
            itr += 1

        return deafCount

    def withinAudibleRange(itrPepShout, itr):
        x1FirstPerson, y1FirstPerson, shoutRadius = Coordinates[itrPepShout]
        x2SecondPerson, y2SecondPerson, _ = Coordinates[itr]
        
        
        return ((x1FirstPerson - x2SecondPerson) ** 2 + (y1FirstPerson - y2SecondPerson) ** 2)  <= shoutRadius**2

    lenPepopleShout = len(Coordinates)
    visited = [False] * lenPepopleShout
    maxDeafCount = 0

    itrPepShout = 0
    while itrPepShout < len(Coordinates):
        if not visited[itrPepShout]:
            maxDeafCount = max(maxDeafCount, findMaxDeaf(itrPepShout, []))
        itrPepShout += 1


    return maxDeafCount

# Example usage:
Coordinates1 = [[1, 2, 11], [10, 10, 2]]
print(MaximumDeafPeople(Coordinates1))  # Output: 1

Coordinates2 = [[2, 1, 4], [6, 1, 2]]
print(MaximumDeafPeople(Coordinates2))  # Output: 2
