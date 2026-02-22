## Selection sort- Find the minimum and swap
## Selection sort brings the minimum element to start of the array

def selection_sort(arr):
    n =len(arr)

    ## Traverse through the array elements till n-2 index
    for i in range(n-1):
        min_index =i

        ## Find the minimum element in the remaining array
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j ## Update the min_index if the smaller element is found

        ## Swap the found minimum with the first element of the unsorted path
        arr[i],arr[min_index] = arr[min_index],arr[i]

    print(f"After selection sort:{arr}")

## Driver code
arr = [13,46,24,52,20,9]

## Print before sorting
print("Before selection sort:")
print(*arr)

selection_sort(arr)


