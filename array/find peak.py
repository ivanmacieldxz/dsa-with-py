""" Find the index of a peak element in an array. An element is a peak if its neighbours are smaller."""

# Naive strategy: go through till find a peak
def find_peak_naive(arr, n):
    # base case: n = 1 -> the only element in the array is the peak
    if n == 1:
        return 0
    
    # base case: n = 2 -> the greatest element from the two is the peak
    if n == 2:
        if arr[0] > arr[1]:
            return 0
        else:
            return 1
    
    # general case: n > 2 -> go through the array till a peak is found
    for index in range(n):
        if index != n-1:
            if arr[index] > arr[index + 1]:
                return_index = index
                break
        else:
            return_index = index
    
    return return_index

# binary search strategy: 
def peak_recursive(arr, start, end, n):
    mid = (start + end) / 2

    # compare with neighbours if possible
    if mid != 0:
        # if it's not the first element and it's bigger than the previous
        if arr[mid] > arr[mid - 1]:
            # if it's the last element, return it as the result
            if mid == n:
                return mid
            else

    


def main():
    arr = [10, 20, 15, 2, 23, 90, 67]
    print(f"Peak in arr: {find_peak_naive(arr, len(arr))}")

if __name__ == "__main__":
    main()