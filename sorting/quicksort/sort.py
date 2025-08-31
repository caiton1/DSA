from random import randint

# ===== QUICK SORT REVIEW ===== #
EVEN_ARR = [47, 3, 89, 15, 62, 28, 96, 54, 7, 71] # len = 10
ODD_ARR = [12, 84, 39, 68, 25, 77, 90, 33, 56, 4, 61] # len = 11

def naive(arr, l, r):
    # temp array approach
    temp = [0] *  (r - l + 1) 
    pivot = arr[l]
    idx = 0 # Tracks pointer
    
    # lesser to left of pivot
    for i in range(l, r + 1):
        if arr[i] < pivot: 
            temp[idx] = arr[i]
            idx += 1
    
    pivot_pos = idx + l
     
    # more to right of pivot
    for i in range(l, r + 1):
        if arr[i] >= pivot:
            temp[idx] = arr[i]
            idx += 1
            
    # copy to origional array
    for i in range(r - l + 1):
        arr[l + i] = temp[i]
    # return pivot index
    return pivot_pos
    
def naive_driver(arr, l, r):
    if l < r:
        pivot_index = naive(arr, l, r)
        naive_driver(arr, l, pivot_index - 1)
        naive_driver(arr, pivot_index + 1, r) 
    
def main():
    array = EVEN_ARR[:]
    print("Before: ", array)
    naive_driver(array, 0, len(array) - 1)
    print("After: ", array)
    print("Sorted? ", array == sorted(array))
        
if __name__ == "__main__":
    main()