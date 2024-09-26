from typing import List

def find_duplicate(nums: List[int]) -> int:
    for num in nums:
        index = abs(num) - 1   
        if nums[index] < 0:   
            return abs(num)
        nums[index] = -nums[index]   

    return -1  
