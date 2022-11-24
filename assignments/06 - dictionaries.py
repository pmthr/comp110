# Practice with dictionaries

def invert(input: dict[str, str]) -> dict[str, str]:
    # Inverts keys with values in a dictionary
    flipped: dict[str, str] = dict()
    for key in input:
        if input[key] in flipped:
            raise KeyError(f"Duplicate key found: {input[key]}")
        flipped[input[key]] = key
    return flipped

def favorite_color(input: dict[str, str]) -> str:
    # Returns the most common color among a dictionary of colors
    counts: dict[str, int] = dict()
    favorite: str = ""
    max: int = 0
    for person in input:
        color = input[person]
        if color not in counts:
            counts[color] = 1
        else:
            counts[color] += 1
    for color in counts:
        if counts[color] > max:
            max = counts[color]
            favorite = color
    
    return favorite

def count(input: list[str]) -> dict[str, int]:
    # Returning the frequency of values in a dictionary
    counts: dict[str, int] = dict()
    for item in input:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1
    return counts

# Unit tests for dictionary functions

def test_invert_edge() -> None:
    # Testing upper/lowercase difference in keys
    assert invert({"kris": "jordan", "michael": "Jordan"}) == {"Jordan": "michael", "jordan": "kris"} 

def test_invert_use1() -> None:
    # Testing invert with characters
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}

def test_invert_use2() -> None:
    # Testing invert with words
    assert invert({"apple": "cat"}) == {"cat": "apple"}

def test_favorite_color_edge() -> None:
    # Testing tiebreaker for colors
    assert favorite_color({"Becca": "green", "Harrison": "yellow", "Pooja": "green", "Annie": "yellow"}) == "green"

def test_favorite_color_use1() -> None:
    # Testing fewer colors
    assert favorite_color({"Becca": "green", "Harrison": "red", "Pooja": "red"}) == "red"

def test_favorite_color_use2() -> None:
    # Testing many colors
    assert favorite_color({"Becca": "orange", "Harrison": "purple", "Pooja": "yellow", "Marc": "yellow", "Kris": "blue"}) == "yellow"

def test_count_edge() -> None:
    # All colors are only 1 each
    assert count(["b", "d", "f"]) == {"b": 1, "d": 1, "f": 1}

def test_count_use1() -> None:
    # Testing smaller list
    assert count(["a", "b", "b"]) == {"a": 1, "b": 2}

def test_count_use2() -> None:
    # Testing larger list
    assert count(["a", "c", "c", "d", "e", "e", "f", "g", "g", "h", "i"]) == {"a": 1, "c": 2, "d": 1, "e": 2, "f": 1, "g": 2, "h": 1, "i": 1}