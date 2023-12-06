def find_path(stone_inscription_list):
    stepCountMatrix=[float('inf')]*len(stone_inscription_list)
    stepCountMatrix[0]=0  
    for i in range(0,len(stone_inscription_list),1):
        for j in range(i + 1,len(stone_inscription_list),1):
            if j-i<=stone_inscription_list[i]:
                stepCountMatrix[j]=min(stepCountMatrix[j],stepCountMatrix[i]+1)
    return stepCountMatrix[-1]




