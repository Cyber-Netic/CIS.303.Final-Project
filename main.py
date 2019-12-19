from typing import List

def binarySearch (arr: List, l, r, x):
    if r >= l:
        # Check base case
        mid = l + (r - l) / 2
        mid = round(mid)
        mid = int(mid)
        if arr[mid] == x:
            # If element is present at the middle itself 
            return mid
        elif arr[mid] > x:
            # If element is smaller than mid, then it 
            # can only be present in left subarray 
            return binarySearch(arr, l, mid - 1, x) 
        else:
            # Else the element can only be present 
            # in right subarray 
            return binarySearch(arr, mid + 1, r, x) 

    else: 
        # Element is not present in the array 
        return -1

# Test ray 
arr = [12, 93, 24, 40, 81, 77, 95]
x = 77

# Function call 
result = binarySearch(arr, 0, len(arr) - 1, x) 

if result != -1: 
    print(f"Element is present at index {result}")
else: 
    print("Element is not present in array")