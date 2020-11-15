


def search(nums, target) -> int:
    """
    https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
    :param nums:
    :param target:
    :return:
    """
    l = 0
    h = len(nums) - 1

    while l <= h:
        m = (l + h) // 2
        if nums[m] == target:
            return m

        if target > nums[m]:
            if target > nums[h] > nums[m]:
                h = m - 1
            else:
                l = m + 1
        elif target < nums[l] <= nums[m]:
            l = m + 1
        else:
            h = m - 1
    return -1


arr =  [4,5,6,7,0,1,2]
x = 0
print(search(arr, x))

