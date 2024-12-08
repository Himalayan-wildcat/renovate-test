def add_one(n: int) -> int:
    """Return the argument incremented by one.

    Args:
        n (int): The number to increment.

    Returns:
        int: The argument incremented by one.

    Raises:
        TypeError: If n is not an integer.

    """
    if not isinstance(n, int):
        raise TypeError(f"n must be int, not {type(n)}")
    return n + 1


def minus_one(n: int) -> int:
    """Return the argument decremented by one.

    Args:
            n (int): The number to decrement.

    Returns:
            int: The argument decremented by one.

    Raises:
            TypeError: If n is not an integer.

    """
    if not isinstance(n, int):
        raise TypeError(f"n must be int, not {type(n)}")
    return n - 1


if __name__ == "__main__":
    pass
