# Basic functions implemented via recursion.

def maxItem(arr):
    if len(arr) == 2: return arr[0] if arr[0] > arr[1] else arr[1]
    subMaximum = max(arr[1:])
    return arr[0] if arr[0] > subMaximum else subMaximum

def countItems(arr):
    if arr == []: return 0
    else: return 1 + countItems(arr[1:])

def summation(arr):
    if arr == []: return 0
    else: return arr[0] + summation(arr[1:])

if __name__ == '__main__':
    l = [int(i) for i in input().split()]
    print(f'Total items: {countItems(l)}')
    print(f'Sum of items: {summation(l)}')
    print(f'Max: {maxItem(l)}')