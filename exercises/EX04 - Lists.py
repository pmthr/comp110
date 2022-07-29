# List utility functions

def all(intlist: list[int], check: int) -> bool:
    # Checks if a given list only consists of a given integer
    i: int = 0 
    if len(intlist) == 0:
        return False
    else:
        while i < len(intlist):
            if intlist[i] != check:
                return False
            i += 1
    return True

def is_equal(list1: list[int], list2: list[int]) -> bool:
    # Checks if two integer lists contain the same values
    i: int = 0
    j: int = 0
    if len(list1) != len(list2):
        return False
    while i < len(list1):
        if list1[i] != list2[j]:
            return False
        j += 1
        i += 1
    return True

def max(input: list[int]) -> int:
    # Returns the largest value in a list
    largest: int = input[0]
    i: int = 0
    j: int
    if len(input) < 1:
        raise ValueError("max() arg is an empty list")
    while i < len(input):
        if input[i] > largest:
            largest = input[i]
        i += 1
    return largest