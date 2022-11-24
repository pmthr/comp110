# List utility functions part 2.

def only_evens(input: list[int]) -> list[int]:
    """Return the even elements of a list."""
    i: int = 0
    evens: list[int] = []
    while i < len(input):
        if input[i] % 2 == 0:
            evens.append(input[i])
        i += 1
    return evens


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Create a sublist of an original list."""
    sublist: list[int] = []
    i: int = 0
    if start < 0:
        i = 0
    else:
        i = start
    if end > len(input):
        end = len(input)
    while i < end:
        sublist.append(input[i])
        i += 1
    return sublist


def concat(firstlist: list[int], secondlist: list[int]) -> list[int]:
    """Concatenate 2 lists together."""
    concat: list[int] = []
    i: int = 0
    while i < len(firstlist):
        concat.append(firstlist[i])
        i += 1
    j: int = 0
    while j < len(secondlist):
        concat.append(secondlist[j])
        j += 1
    return concat


# Unit tests for list utility functions

def test_only_evens_edge() -> None:
    """All numbers are odd. Should return empty list."""
    test: list[int] = [3, 5, 7, 9, 1]
    assert only_evens(test) == []


def test_only_evens_use1() -> None:
    """Testing multiple items with 0s in the list. 0s are even!"""
    test: list[int] = [6, 0, 3, 0, 4]
    assert only_evens(test) == [6, 0, 0, 4]
    

def test_only_evens_use2() -> None:
    """Test with multiple items, both odd and even, no 0s."""
    test: list[int] = [6, 3, 5, 4, 8, 9, 2]
    assert only_evens(test) == [6, 4, 8, 2]


def test_sub_edge() -> None:
    """Test empty list."""
    test: list[int] = []
    assert sub(test, 2, len(test)) == []


def test_sub_use1() -> None:
    """Test normal use."""
    test: list[int] = [5, 4, 3, 2, 6]
    assert sub(test, 1, 3) == [4, 3]


def test_sub_use2() -> None:
    """Testing the sub list being the same as original list."""
    test: list[int] = [2, 3, 4]
    assert sub(test, 0, 3) == [2, 3, 4]


def test_concat_edge() -> None:
    """One list is empty."""
    test: list[int] = [5, 4, 6]
    test2: list[int] = []
    assert concat(test, test2) == [5, 4, 6]

def test_concat_use1() -> None:
    """2 Small lists."""
    test: list[int] = [2, 3]
    test2: list[int] = [1]
    assert concat(test, test2) == [2, 3, 1]

def test_concat_use2() -> None:
    """2 Larger lists."""
    test: list[int] = [3, 4, 2, 5, 6, 7]
    test2: list[int] = [3, 2, 1, 3]
    assert concat(test, test2) == [3, 4, 2, 5, 6, 7, 3, 2, 1, 3]

