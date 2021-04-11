def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lessNum, moreNum = [], []
        for i in arr:
            if i > pivot: moreNum.append(i)
            elif i < pivot: lessNum.append(i)
        return quickSort(lessNum) + [pivot] + quickSort(moreNum)


l = list(map(int, input("Enter a list of numbers: ").split()))
print(f'The sorted array: {quickSort(l)}')