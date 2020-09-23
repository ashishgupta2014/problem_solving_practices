def insertion(arr):
    for i in range(len(arr)):
        if arr[i] < arr[0]:
            arr[0], arr[i] = arr[i], arr[0]
        else:
            for j in range(1, i):
                if arr[j - 1] < arr[i] < arr[j]:
                    arr[j], arr[j+1] = arr[i], arr[j]

