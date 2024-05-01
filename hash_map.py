
from typing import Callable
from my_list import MyList, my_list_create, my_list_put, my_list_get, my_list_del, my_list_each

# HashMap = list[MyList]
HashMap = list[MyList|None]

def hash_algorithm(s) -> int:
    current_value = 0

    for char in s:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256

    return current_value

# hash_map_create
# hash_map_put
# hash_map_get
# hash_map_del
# hash_map_each

def hash_map_create():
    return [None for _ in range(8)]
    # return []

def hash_map_put(hash_map:HashMap, key:str, value:int) -> None:
    """
    >>> h = hash_map_create()
    >>> hash_map_put(h, "k2", 3)
    >>> hash_map_put(h, "k1", 1)
    >>> hash_map_put(h, "k1", 3)
    >>> hash_map_get(h, "k1")
    3
    >>> hash_map_get(h, "k2")
    3
    """
    index = hash_algorithm(key) % len(hash_map)
    x = hash_map[index]

    if x is None:
        hash_map[index] = x = my_list_create()

    my_list_put(x, key, value)

def hash_map_get(hash_map:HashMap, key:str) -> int|None:
    """
    >>> h = hash_map_create()
    >>> hash_map_put(h, "k1", 1)
    >>> hash_map_get(h, "k1")
    1
    >>> hash_map_get(h, "k2")
    """

    index = hash_algorithm(key) % len(hash_map)

    if index < len(hash_map):
        x = hash_map[index]
        if x is not None:
            return my_list_get(x, key)

    return None

def hash_map_del(hash_map:HashMap, key:str) -> None:

    index = hash_algorithm(key) % len(hash_map)
    if index < len(hash_map):
        x = hash_map[index]
        if x is not None:
            my_list_del(x, key)

def hash_map_each(hash_map:HashMap, func: Callable[[str, int], None]) -> None:
    """
    >>> h = hash_map_create()
    >>> hash_map_put(h, "k1", 1)
    >>> hash_map_put(h, "k2", 2)
    >>> def my_func(key, value) -> None:
    ...     print(key, value)
    ...     return
    >>> hash_map_each(h, my_func)
    k1 1
    k2 2
    """
    for my_list in hash_map:
        if my_list is not None:
            my_list_each(my_list, func)
