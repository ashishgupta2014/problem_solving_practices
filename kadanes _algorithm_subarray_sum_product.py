from rope.base.builtins import List


def maxProduct(nums: List) -> int:
    ## RC ##
    ## APPROACH : KADANES ALGORITHM ##

    ## TIME COMPLEXITY : O(N) ##
    ## SPACE COMPLEXITY : O(1) ##

    # 1. Edge Case : Negative * Negative = Positive
    # 2. So we need to keep track of minimum values also, as they can yield maximum values.

    global_max = prev_max = prev_min = nums[0]
    for num in nums[1:]:
        curr_min = min(prev_max * num, prev_min * num, num)
        curr_max = max(prev_max * num, prev_min * num, num)
        global_max = max(global_max, curr_max)
        prev_max = curr_max
        prev_min = curr_min
    return global_max
print(maxProduct([2,3,-2,4, 0 , 87, -1]))