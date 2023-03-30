# given the heights of towers find the max amount of water that can be stored in them
# https://leetcode.com/problems/trapping-rain-water/

def sol(heights):
    if not heights:
        return 0
    
    l, r = 0, len(heights) - 1
    l_max, r_max = heights[l], heights[r]
    total_rain = 0

    while l < r:
        if heights[l] < heights[r]:
            l+=1
            l_max = max(l_max, heights[l])
            total_rain += l_max - heights[l]
        else:
            r+=1
            r_max = max(r_max, heights[r])
            total_rain += r_max - heights[r]

    return total_rain

print(sol([4,2,0,3,2,5])) #9