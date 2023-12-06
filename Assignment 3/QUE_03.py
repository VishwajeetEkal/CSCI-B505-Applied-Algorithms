def makeNumber(length_of_number, K, cn):
        if length_of_number == 0:
            return [cn]
        answerNumbers = []
        
        if cn % 10 + K <= 9:
            answerNumbers += makeNumber(length_of_number - 1, K, cn * 10 + cn % 10 + K)
        
        if K != 0 and cn % 10 >= K:
            answerNumbers += makeNumber(length_of_number - 1, K, cn * 10 + cn % 10 - K)
        
        return answerNumbers
    
def zenthar_puzzle( N,K):
    if N <= 0 or K < 0:
        return []
    
    result = []
    i = 1
    while i <10:
        result += makeNumber(N - 1, K, i)
        i+=1

    result.sort()

    return result

print(zenthar_puzzle(3,8))

