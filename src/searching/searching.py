# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) == 0:
        return -1

    if end - start <= 1:
        if arr[start] == target:
            return start
        elif arr[end] == target:
            return end
        else: 
            return -1
    else:
        mid = int((start + end) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid)
        elif arr[mid] < target:
            return binary_search(arr, target, mid, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

