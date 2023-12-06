import heapq 
import copy

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

def cheapest_path(N, costs, start):

    costToTravel = {itr: float('inf') for itr in range(N)}
    costToTravel[start] = 0

    costPq = [(0, start)]

    while costPq:
        
        currentPrice, currentPoint = heapq.heappop(costPq)

        
        if currentPrice > costToTravel[currentPoint]:
            continue

        
        for price in enumerate(costs[currentPoint]):

            if price[1] == 0:
                continue
            newPrice = currentPrice + price[1]

            if newPrice < costToTravel[price[0]]:
                costToTravel[price[0]] = newPrice
                heapq.heappush(costPq, (newPrice, price[0]))

    return list(costToTravel.values())

def generate_password(word_list):
    word_list_copy = copy.deepcopy(word_list)
    word_list_copy.sort()
    while len(word_list_copy) > 1:
        best_overlap_length = 0
        best_positions = (0, 1)

        for idx_1 in range(len(word_list_copy)):
            
            for idx_2 in range(idx_1 + 1, len(word_list_copy)):
                
                overlap_length = find_overlap(word_list_copy[idx_1], word_list_copy[idx_2])
                if overlap_length > best_overlap_length:
                    best_overlap_length = overlap_length
                    best_positions = (idx_1, idx_2)

        pos_1, pos_2 = best_positions
        if word_list_copy[pos_1] in word_list_copy[pos_2]:
            combined_word = word_list_copy[pos_2]
        elif word_list_copy[pos_2] in word_list_copy[pos_1]:
            combined_word = word_list_copy[pos_1]
        else:
            combined_word = combine_words(word_list_copy[pos_1], word_list_copy[pos_2], best_overlap_length)
        word_list_copy.pop(pos_2)
        word_list_copy[pos_1] = combined_word

    return word_list_copy[0]

def find_overlap(firstStr, secondStr):
    best_overlap_length = 0
    min_len = min(len(firstStr), len(secondStr))

    for i in range(1, min_len):
        if firstStr.endswith(secondStr[:i]):
            best_overlap_length = i

    return best_overlap_length

def combine_words(firstStr, secondStr, overlap):
    return firstStr + secondStr[overlap:]


def smallestString(givenWord):
    givenWord = list(givenWord)
    encodeLength = len(givenWord)
    
    itrGivenWord = 0
    while itrGivenWord < encodeLength // 2:
        if givenWord[itrGivenWord] != 'a':
            givenWord[itrGivenWord] = 'a'
            return ''.join(givenWord)
        itrGivenWord += 1
    
    
    givenWord[-1] = 'b'
    return ''.join(givenWord)

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


def grandTour(connections):
    def is_valid(v, pos, p, marked):
        if connections[p[pos - 1]][v] == 0:
            return False
        if marked[v]:
            return False
        return True

    def hamiltonian_util(pos):
        if pos == num_vertices:
            return connections[p[pos - 1]][p[0]] == 1

        for v in range(1, num_vertices):
            if is_valid(v, pos, p, marked):
                p[pos] = v
                marked[v] = True

                if hamiltonian_util(pos + 1):
                    return True

                p[pos] = -1
                marked[v] = False

        return False

    num_vertices = len(connections)
    p = [-1] * num_vertices
    marked = [False] * num_vertices

    p[0] = 0
    marked[0] = True

    if not hamiltonian_util(1):
        return False

    if connections[p[num_vertices - 1]][p[0]] == 0:
        return False

    return True
