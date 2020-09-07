def solution(nums):
    max_res = len(nums) // 2
    num_set = len(set(nums))
    return min(max_res,num_set)