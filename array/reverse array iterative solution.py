"""Write a program to reverse an array or string"""
#Time complexity: O(n), auxiliary space: O(n)
def reverse_array(arr):
    size = len(arr)
    
    reversed = [None] * size

    #for each index in the array
    for index in range(size):
        #assign the element to the corresponding index in reversed
        reversed[size - 1 - index] = arr[index]

    return reversed

#Another way, with O(1) auxiliary space:
def reverse_array_no_aux_space(arr):
    #get size of the array
    size = len(arr)

    #for each index
    for index in range(int(size/2)):
        #swap arr[index] for arr[size - index - 1]
        aux = arr[index]
        arr[index] = arr[size - index - 1]
        arr[size - index - 1] = aux
        #alternatively could have done:
        #arr[index], arr[size-index-1] = arr[size-index-1], arr[index]
    
    #no need to return, since reference has been modified


def main():
    size = 0
    
    #asking for a valid array size
    while size <= 0:
        size = int(input("Enter number of elements of the array: "))
    
    #declare array with default values
    arr = [None] * size

    #asking for the values of each index
    for x in range(size):
        arr[x] = input(f"Enter {x+1}° element: ")
    
    reverse_array_no_aux_space(arr)
    #print reversed array
    print(f"Reversed array: {arr}")

if __name__ == "__main__":
    main()