# Utility functions

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], col_name: str) -> list[str]:
    """Produce a list of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[col_name]
        result.append(item)
    return result

def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table into a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result

def head(col_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a column oriented table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for key in col_table:
        i: int = 0
        if rows > len(col_table[key]):
            return col_table
        temp_list: list[str] = []
        while i < rows:
            temp_list.append(col_table[key][i])
            i += 1
        result[key] = temp_list
    return result


def select(col_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column based table with a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for name in names:
        result[name] = col_table[name]
    return result


def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based table with two column based tables combined."""
    result: dict[str, list[str]] = {}
    for key in first_table:
        result[key] = first_table[key]
    for key in second_table:
        if key not in result:
            result[key] = second_table[key]
        else:
            result[key] = first_table[key] + second_table[key]
    return result


def count(to_count: list[str]) -> dict[str, int]:
    """Produce a dictionary where each key is a unique value in the given list and each value associated is the frequency of that value in the list."""
    result: dict[str, int] = {}
    for value in to_count:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result