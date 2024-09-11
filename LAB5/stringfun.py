def count_char(string, char):
    """
    >>> count_char("hello", "l")
    2
    >>> count_char("Hello", "H")
    1
    >>> count_char("ab d e", " ")
    2
    """
    t = 0
    try:
        for i in string:
            if i == char:
                t += 1
        return t
    except ValueError:
        return "You must insert String values as inputs"


def remove(string, index):
    """
    >>> remove("hello", 1)
    'hllo'
    >>> remove("world", 4)
    'worl'
    >>> remove("test", 2)
    'tet'
    """
    a = []
    ans = ""
    for i, j in enumerate(string): 
        if i != index:
            a.append(j)
    for i in a:
        ans += i
    return ans


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)

