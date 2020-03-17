# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    #Set values for a while loop
    a = b = c = 0

    #While both arrays lengths are greater than 0 (to start)
    while a < len(arrA) and b < len(arrB):
        #If the first element in arrA is less than the first element in arrB
        if (arrA[a] < arrB[b]):
            #Then the first element in a new array will be equal to the first element in arrA
            merged_arr[c] = arrA[a]
            #Add values to "a" and "c" in order to iterate through different indexes next time
            a += 1
            c += 1
        #Otherwise (if the element in arrB was lower)
        else:
            #Make the first element in the new array equal to arrB's first element instead
            merged_arr[c] = arrB[b]
            #Update values in order to iterate through different indexes next time
            b += 1
            c += 1
    #While the value of "a" (which is used to iterate through indexes) is less than the length of arrA
    while a < len(arrA):
        #The value of "c"(used to keep track of how many times youve added values to the new array) equals the value in arrA
        merged_arr[c] = arrA[a]
        a += 1
        c += 1
    #While the value of "b" (which is used to iterate through indexes) is less than the length of arrB
    while b < len(arrB):
        #The value of "c"(used to keep track of how many times youve added values to the new array) equals the value in arrB
        merged_arr[c] = arrB[b]
        b += 1
        c += 1
    
    return merged_arr




# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2 :])
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
