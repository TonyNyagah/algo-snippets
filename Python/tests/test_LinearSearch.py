from Searching.LinearSearch import LinearSearch


def test_answer():
    ls: list = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420];
    assert LinearSearch(ls, 69) == True
    assert LinearSearch(ls, 1336) == False
    assert LinearSearch(ls, 420) == True
    assert LinearSearch(ls, 69420) == True
    assert LinearSearch(ls, 69421) == False
    assert LinearSearch(ls, 1) == True
    assert LinearSearch(ls, 0) == False
