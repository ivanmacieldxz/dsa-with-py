""" Given an array of size N, find the maximum and the minimum element of the array using the minimum number of comparisons, it is required to return both values from the function """

# structure named pair
class Pair:
    def __init__(self):
        self.min = None
        self.max = None

# exhaustive search approach
# time complexity: O(n), auxiliary space: O(1)
def minmax_in_arr_linear_search(arr, n):
    minmax = Pair()

    # if the array only has one element, return it as both min and max
    if n == 1:
        minmax.max = minmax.min = arr[0]
        return minmax
    
    # if it has more than one elements, then initialize min and max accordingly
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]
    
    # search through the rest of the array
    for index in range(2, n):
        aux = arr[index]
        if aux > minmax.max:
            minmax.max = aux
        elif aux < minmax.min:
            minmax.min = aux
    
    return minmax

# tournament method is based on dividing the array recursively in halves and finding each half maximum and minimum
def minmax_with_tournament_method(arr, n):
    minmax = Pair()
    
    # especial case: original array of size 1
    if n == 1:
        minmax.min = minmax.max = arr[0]
    # recursion base case: array of size 2, only one comparison needed to get min and max
    elif n == 2:
        if arr[0] > arr[1]:
            minmax.max = arr[0]
            minmax.min = arr[1]
        else:
            minmax.max = arr[1]
            minmax.min = arr[0]
    # recursive case: 
    else:
        # get mid as floor
        mid = (n - 1) // 2 + 1


    return minmax