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


def binarySearchRecurse(arr, item):
  # Base case
  if len(arr) == 1: return arr[0] if arr[0] == item else 'Item not found.'

  # Recursive case
  if arr[len(arr)//2] == item: return f'{item} found at index {len(arr)//2}'    
  elif arr[len(arr)//2] > item: return binarySearchRecurse(arr[:len(arr)//2-1], item)
  elif arr[len(arr)//2] < item: return binarySearchRecurse(arr[len(arr)//2+1:], item)
    

l = [int(i) for i in input("Enter a list: ").split()]
item = int(input("Enter the item to search: "))
print(binarySearchRecurse(l, item))