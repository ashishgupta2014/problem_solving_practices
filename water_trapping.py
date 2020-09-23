def trap(nums):
    h = len(nums) - 1
    l = 0
    rs = 0
    lf = 0
    rt = 0
    while l <= h:
        if nums[l] < nums[h]:
            if lf < nums[l]:
                lf = nums[l]
            else:
                rs = rs + lf - nums[l]
            l += 1
        else:
            if rt < nums[h]:
                rt = nums[h]
            else:
                rs = rs + rt - nums[h]
            h -= 1
    return rs

a=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(a))