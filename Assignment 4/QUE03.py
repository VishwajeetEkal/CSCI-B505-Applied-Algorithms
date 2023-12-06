def smallest_missing_Number(streetNumbers, lower, upper):
        if lower > upper:
            return lower

        m = int((lower + upper)/2)

        if streetNumbers[m] > m:
            
            return smallest_missing_Number(streetNumbers, lower, m - 1)
            
        else:
            
            return smallest_missing_Number(streetNumbers, m + 1, upper)


def smallestMissingNumber(streetNumbers):
    
    return smallest_missing_Number(streetNumbers, 0, len(streetNumbers) - 1)


print(smallestMissingNumber([0,1,2,3,5,6]))