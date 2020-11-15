def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


def binay_search_itr(arr, x):
    """

    :param arr:
    :param x:
    :return:
    """
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = l + (h - l // 2)
        if arr[m] == x:
            return m
        elif arr[m] > x:
            m -= 1
            h = m
        else:
            m += 1
            l = m
    else:
        return -1
print(binay_search_itr(arr, x))
