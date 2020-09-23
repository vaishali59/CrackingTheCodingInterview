def search(strings, target, l, r):
    if l > r:
        return -1
    mid = (l+r)//2
    if strings[mid] == "":
        left = mid-1
        right = mid+1
        while True:
            if left < l and right > r:
                return -1
            elif left >= l and strings[l] != "":
                mid = l
                break
            elif right <= r and strings[r] != "":
                mid = r
                break
            l -= 1
            r += 1
    if strings[mid] == target:
        return mid
    elif target < strings[mid]:
        return search(strings, target, l, mid-1)
    else:
        return search(strings, target, mid+1, r)


def sparseSearch(strings, target):
    if not strings or not target or target == "":
        return -1
    return search(strings, target, 0, len(strings)-1)


stringslist = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
print(sparseSearch(stringslist, "car"))


