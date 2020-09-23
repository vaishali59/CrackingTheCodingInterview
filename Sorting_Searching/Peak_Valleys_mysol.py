def peakValleys(arr):
    up = False
    down = False

    for k in range(len(arr)-1):
        if not up and not down:
            if arr[k]>arr[k+1]:
                up = not up
            elif arr[k]<arr[k+1]:
                down = not down
            else:
                return -1
        elif down:
            if arr[k]==arr[k+1]:
                return -1
            if arr[k] < arr[k+1]:
                arr[k],arr[k+1]=arr[k+1],arr[k]
            up = not up
            down = not down
        elif up:
            if arr[k]==arr[k+1]:
                return -1
            if arr[k] > arr[k+1]:
                arr[k],arr[k+1]=arr[k+1],arr[k]
            down = not down
            up = not up
        else:
            return -1
    return arr

arr = [3,5,5,7,8]
print(peakValleys(arr))


        
