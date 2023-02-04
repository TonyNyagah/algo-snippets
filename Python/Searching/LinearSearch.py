# most basic search algo
# Time Complexity: O(n)
def LinearSearch(ls: list, target: int) -> bool:
    for i in range(len(ls)):
        if ls[i] == target:
            return True
    return False