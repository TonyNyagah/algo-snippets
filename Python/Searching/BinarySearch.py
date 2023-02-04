# Time Complexity: O(log n)
# the list has to be sorted
def BinarySearch(ls: list, target: int) -> bool:
    low = 0
    high = len(ls)

    while low < high:
        mid = (low + high) // 2
        if ls[mid] == target:
            return True
        elif ls[mid] > target:
            high = mid
        else:
            low = mid + 1

    return False
            
