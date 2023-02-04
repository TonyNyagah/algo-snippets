from Searching.BinarySearch import BinarySearch


def test_answer():
    ls: list = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420];
    assert BinarySearch(ls, 69) == True
    assert BinarySearch(ls, 1336) == False
    assert BinarySearch(ls, 420) == True
    assert BinarySearch(ls, 69420) == True
    assert BinarySearch(ls, 69421) == False
    assert BinarySearch(ls, 1) == True
    assert BinarySearch(ls, 0) == False
