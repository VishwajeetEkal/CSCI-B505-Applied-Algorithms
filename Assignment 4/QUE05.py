def place_max_speedbump(len_road, bump_int1, bump_int2, bump_int3):

    nums =[bump_int1, bump_int2, bump_int3]
    dp = [None] * (len_road + 1)
    dp[0] = []

    for i in range(1, len_road + 1):
        for num in nums:
            if i - num >= 0 and dp[i - num] is not None and (dp[i] is None or len(dp[i - num]) + 1 > len(dp[i])):
                dp[i] = dp[i - num] + [num]
    #print(dp)
    return dp[-1]

print(place_max_speedbump(7, 2, 3, 5)) 
print(place_max_speedbump(5, 2, 1, 2)) 
print(place_max_speedbump(13, 5, 5, 7))  
print(place_max_speedbump(13, 5, 3, 2))  
print(place_max_speedbump(13, 5, 3, 7))  


