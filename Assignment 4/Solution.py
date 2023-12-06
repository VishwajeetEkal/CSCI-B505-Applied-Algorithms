def MinimumExpenditure(AppleTreePrice):
    lenTree = len(AppleTreePrice)
    for itTree in range(1, lenTree):
        for itCost in range(3):
            mininumCost = min(AppleTreePrice[itTree-1][(j % 3)] for j in range(3) if j != itCost)
            AppleTreePrice[itTree][itCost] += mininumCost

    return min(AppleTreePrice[-1])

def alignments(A, B):
    count_matrix = [[0]*(B+1)for _ in range(A+1)]
    for itrA in range(A+1):
        count_matrix[itrA][0]=1
    for itrB in range(B+1):
        count_matrix[0][itrB]=1
    for itrA in range(1, A+1):
        for itrB in range(1, B+1):
            count_matrix[itrA][itrB]=count_matrix[itrA-1][itrB]+count_matrix[itrA][itrB-1]+count_matrix[itrA-1][itrB-1]
    return count_matrix[-1][-1]


def smallestmissingNumber(streetNumbers, lower, upper):
        if lower>upper:
            return lower
        midpoint = int((lower+upper)/2)
        if streetNumbers[midpoint]>midpoint:
            return smallestmissingNumber(streetNumbers,lower,midpoint - 1)
        else:
            return smallestmissingNumber(streetNumbers,midpoint + 1,upper)


def smallestMissingNumber(streetNumbers):  
    return smallestmissingNumber(streetNumbers, 0, len(streetNumbers) - 1)

def divide(max, numbs):
        dvde=1
        csum=0
        for numItr in numbs:
            csum += numItr
            if max<csum:
                dvde+= 1
                csum=numItr
        return dvde

def solution_inheritance(num_items, num_boxes, children):
    if children>num_boxes or children==0:
         return -1
    low, high=max(num_items),sum(num_items)  
    while low<high:
        mid=int((low + high)/2)
        dvde=divide(mid, num_items)
        if dvde<=children:
            high=mid
        else:
            low=mid+1
    return low

def place_max_speedbump(len_road, bump_int1, bump_int2, bump_int3):
    bumpMatrix =[0]+[-1]*len_road  
    for a in range(1,len_road+1,1):
        if a-bump_int1>=0 and bumpMatrix[a-bump_int1]!=-1:
            bumpMatrix[a]=max(bumpMatrix[a-bump_int1]+1,bumpMatrix[a])
        if a-bump_int2>=0 and bumpMatrix[a-bump_int2]!=-1:
            bumpMatrix[a]=max(bumpMatrix[a-bump_int2]+1,bumpMatrix[a])
        if a-bump_int3>=0 and bumpMatrix[a-bump_int3]!=-1:
            bumpMatrix[a]=max(bumpMatrix[a-bump_int3]+1,bumpMatrix[a])  
    if bumpMatrix[-1]==-1:
        return 0
    return bumpMatrix[-1]

def find_path(stone_inscription_list):
    stepCountMatrix=[float('inf')]*len(stone_inscription_list)
    stepCountMatrix[0]=0  
    for i in range(0,len(stone_inscription_list),1):
        for j in range(i + 1,len(stone_inscription_list),1):
            print(j-i,stone_inscription_list[i])
            if j-i<=stone_inscription_list[i]:
                stepCountMatrix[j]=min(stepCountMatrix[j],stepCountMatrix[i]+1)
    return stepCountMatrix[-1]

def dcdMsg(fs=[],ss=[]):    
        fs_itr,ss_itr =0,0
        temp=[]
        while fs_itr<len(fs) and ss_itr<len(ss):
            if fs[fs_itr]<ss[ss_itr]:
                temp.append(fs[fs_itr])
                fs_itr+=1
            else:
                temp.append(ss[ss_itr])
                ss_itr+=1
        if ss_itr<len(ss):
            temp+=ss[ss_itr:]
        if fs_itr<len(fs):
            temp+=fs[fs_itr:]
        return temp

def decode_cryptic_message(lists):
    dcdd_msg = lists[0]
    for i in range(1,len(lists),1):
        dcdd_msg=dcdMsg(dcdd_msg, lists[i])
    return dcdd_msg
