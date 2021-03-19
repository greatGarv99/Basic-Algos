def binary_search(arr, item):
  low = 0
  high = len(arr)-1

  while low < high:
    mid = (low + high)//2
    mid_val = arr[mid]

    if mid_val == item: return f'{item} found at index {mid}'
    elif mid_val < item: high = mid - 1
    elif mid_val > item: low = mid + 1
  
  return "Item not found."


l = [int(i) for i in input("Enter a list: ").split()]
item = int(input("Enter the item to search: "))
print(binary_search(l, item))