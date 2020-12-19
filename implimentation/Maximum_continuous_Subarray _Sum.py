def subArray(arr):
    """
    https://app.glider.ai/tutorials/maximum-sub-array/problem

    Find out the maximum sub-array of non-negative numbers from an array.
    The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth elements and skipping the third element is invalid.
    The maximum sub-array is defined in terms of the sum of the elements in the sub-array.
    Sub-array A is greater than sub-array B if sum(A) > sum(B).
    Example:
    A : [1, 2, 5, -7, 2, 3]
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3]
    NOTE 1: If there is a tie, then compare with segment's length and return segment which has a maximum length
    NOTE 2: If there is still a tie, then return the segment with a minimum starting index

    Input
    The first line of input contains an integer N, representing the size of the array ar[].
    The second line of input contains N space-separated integers, representing the array elements.

    Output
    Print the Sub-array with maximum sum.

    Constraints
    1 ≤ N ≤ 100
    -100 ≤ ar[i] ≤ 100

    :param arr:
    :return:
    """
    out = {}
    sub_sum = {}
    key = None
    if arr[-1] > 0:
        arr.append(-1)
    for i, ele in enumerate(arr):
        if ele > 0:
            if key is None:
                out[i] = [ele]
                key = i
            else:
                out[key].append(ele)
        else:
            if key is not None:
                sub_sum[key] = {'by_sum': sum(out[key]), 'by_len': len(out[key])}
            key = None
    keys = sorted(sub_sum, key=lambda x: (-sub_sum[x]['by_sum'], -sub_sum[x]['by_len'], x))
    return out[keys[0]]
print(subArray([1, 2, 5, -7, 1, 2, 5, -8, 4]))