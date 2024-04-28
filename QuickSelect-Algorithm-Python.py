import random

def quick_select(arr, left, right, k):
    if left == right:
        return arr[left]
    
    pivot_index = partition(arr, left, right)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_select(arr, left, pivot_index - 1, k)
    else:
        return quick_select(arr, pivot_index + 1, right, k)

def partition(arr, left, right):
    pivot_index = choose_pivot_index(left, right)
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left
    
    for i in range(left, right):
        if arr[i] <= pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    
    arr[store_index], arr[right] = arr[right], arr[store_index]
    return store_index

def choose_pivot_index(left, right):
    return random.randint(left, right)

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 4
print("The", k, "th smallest element is:", quick_select(arr, 0, len(arr) - 1, k))
