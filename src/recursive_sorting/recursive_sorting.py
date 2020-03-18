# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    #Set values for a while loop.
    #values are used to break while loops.
    a = b = c = 0

    #While both arrays lengths are greater than 0 (to start).
    while a < len(arrA) and b < len(arrB):
        #If the first element in arrA is less than the first element in arrB.
        if (arrA[a] < arrB[b]):
            #Then the first element in a new array will be equal to the first element in arrA.
            merged_arr[c] = arrA[a]
            #Add values to "a" and "c" in order to stop iteration.
            a += 1
            c += 1
        #Otherwise (if the element in arrB was lower).
        else:
            #Make the first element in the new array equal to arrB's first element instead.
            merged_arr[c] = arrB[b]
            #Update values in order to stop iteration.
            b += 1
            c += 1
    #While the value of "a" is less than the length of arrA.
    while a < len(arrA):
        #The value of "c" equals the value in arrA.
        merged_arr[c] = arrA[a]
        a += 1
        c += 1
    #While the value of "b" is less than the length of arrB.
    while b < len(arrB):
        #The value of "c" equals the value in arrB.
        merged_arr[c] = arrB[b]
        b += 1
        c += 1
    
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION

#Function that runs first.
def merge_sort(arr):
    #If the length of the given array is greater than 1.
    if len(arr) > 1:
        #"left" = the first element in the array, to half way through the elements.
        left = merge_sort(arr[0:len(arr) // 2])
        #"right" = the last element.
        right = merge_sort(arr[len(arr) // 2:])
        #"arr" = the 2 elements (left and right) to be passed into the merge function above.
        arr = merge(left, right)

    return arr

print(merge_sort([9,7,8,5,6,3,4,1,2]))



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
