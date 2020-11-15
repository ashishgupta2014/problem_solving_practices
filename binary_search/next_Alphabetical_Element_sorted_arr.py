def binay_search_itr(arr, x):
    """
   https://www.geeksforgeeks.org/smallest-alphabet-greater-than-a-given-character/
   Given a list of sorted characters consisting of both Uppercase and Lowercase Alphabets and a particular target value, say K, the task is to find the smallest element in the list that is larger than K.
Letters also wrap around. For example, if K = ‘z’ and letters = [‘A’, ‘r’, ‘z’], then the answer would be ‘A’.
    :param arr:
    :param x:
    :return:
    """
    l = 0
    h = len(arr) - 1
    res = ''
    while l <= h:
        m = l + (h - l // 2)
        if arr[m].lower() == x.lower():
            l = m + 1
        elif arr[m].lower() > x.lower():
            res = arr[m]
            h = m - 1
        else:
            l = m + 1
    return res
print(binay_search_itr(['a', 'b',  'f', 'g'], 'B'))