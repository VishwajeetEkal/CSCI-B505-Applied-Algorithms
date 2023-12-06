def calculateShortBuildings(heights, answerArray):
        if len(heights) <= 1:
            return heights

        mid = len(heights) // 2
        lowerAnsArr = calculateShortBuildings(heights[:mid], answerArray)
        upperAnsArr = calculateShortBuildings(heights[mid:], answerArray)

        shorterBuildings = []
        iterLow, iterUp = 0, 0

        while iterLow < len(lowerAnsArr) or iterUp < len(upperAnsArr):
            if iterUp == len(upperAnsArr) or (iterLow < len(lowerAnsArr) and lowerAnsArr[iterLow] <= upperAnsArr[iterUp]):
                shorterBuildings.append(lowerAnsArr[iterLow])
                answerArray[lowerAnsArr[iterLow][1]] += iterUp
                iterLow += 1
            else:
                shorterBuildings.append(upperAnsArr[iterUp])
                iterUp += 1

        return shorterBuildings

def shorterBuildings(heights):
    heightLength= len(heights)
    answerArray = [0] * heightLength

    heights = [(heights[iterHeight], iterHeight) for iterHeight in range(0,heightLength,1)]  
    calculateShortBuildings(heights, answerArray)

    return answerArray


heights = [5, 4, 3, 2, 6, 3]
output = shorterBuildings(heights)
print(output)  
