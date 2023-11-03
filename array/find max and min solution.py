""" Given an array of size N, find the maximum and the minimum element of the array using the minimum number of comparisons, it is required to return both values from the function """

# import random for testing
import random

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
def minmax_with_tournament_method(arr, initial_index, final_index):
    minmax = Pair()
    
    # especial case: original array of size 1
    if initial_index == final_index:
        minmax.min = minmax.max = arr[0]
    # recursion base case: array of size 2, only one comparison needed to get min and max
    elif final_index == initial_index + 1:
        if arr[0] > arr[1]:
            minmax.max = arr[0]
            minmax.min = arr[1]
        else:
            minmax.max = arr[1]
            minmax.min = arr[0]
    # recursive case: get high and low of left half and high and low of right side 
    else:
        # get mid as floor
        mid = (initial_index + final_index ) // 2
        
        # get min and max from start to mid
        minmax_left_side = minmax_with_tournament_method(arr, initial_index, mid)
        # get min and max of the rest
        minmax_right_side = minmax_with_tournament_method(arr, mid + 1, final_index)

        # compare and replace accordingly:
        if minmax_left_side.min < minmax_right_side.min:
            minmax.min = minmax_left_side.min
        else:
            minmax.min = minmax_right_side.min
        
        if minmax_left_side.max > minmax_right_side.max:
            minmax.max = minmax_left_side.max
        else:
            minmax.max = minmax_right_side.max

    return minmax

def main():
    arr = []

    for i in range(10):
        arr.append(random.randint(0, 150))

    minmax_linear = minmax_in_arr_linear_search(arr, len(arr))
    minmax_t = minmax_with_tournament_method(arr, 0, len(arr) - 1)

    print(f"Array: {arr}.")
    print(f"With linear search method: \n-Max: {minmax_linear.max}\n-Min: {minmax_linear.min}")
    print(f"With tournament method: \n-Max: {minmax_t.max}\n-Min: {minmax_t.min}")

if __name__ == "__main__":
    main()