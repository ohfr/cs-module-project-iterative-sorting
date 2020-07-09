def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low =0
    high = (len(arr)-1)
    found = False

    while (high >= low and not found):
        med = (low+high)//2

        if target == arr[med]:
            found = True
            return med
        else:
            if arr[med] > target:
                high = med-1
            if arr[med] < target:
                low = med+1

    return -1  # not found
