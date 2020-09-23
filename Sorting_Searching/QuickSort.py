arr = [9, 3, 4, 1, 6, 2, 0]


def quickSort(arr, left, right):
    index = partition(arr, left , right)
    if left < index-1:
        quickSort(arr, left, index -1)
    if right > index:
        quickSort(arr, index, right)
    

def partition(arr, left, right):
    pivot = arr[(left + right)//2]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right]>pivot:
            right -=1
        if left<=right:
            if left != right:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
            left +=1
            right -=1
    return left

quickSort(arr, 0, len(arr)-1)
print(arr)
    
