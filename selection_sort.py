def selectionSort(arr):
    sortedArray = []
    while len(arr) != 0:
        item = min(arr)
        sortedArray.append(item)
        arr.remove(item)

    return sortedArray

if __name__ == '__main__':
    l = [int(i) for i in input("Enter a list of numbers: ").split()]
    print(selectionSort(l))