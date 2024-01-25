def sortedSquares(nums):
    l = 0
    r = len(nums)-1
    result = [0]*len(nums)

    for i in range(len(nums)-1,-1,-1):
        if abs(nums[l]) < abs(nums[r]):
            square = nums[r]**2
            r-=1
        else:
            square = nums[l]**2
            l+=1
        result[i] = square
    
    return result

print(sortedSquares([-5,-3,-2,-1]))
