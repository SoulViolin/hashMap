from typing import Callable

MyList = list[tuple[str, int]]
# HashMap = list[MyList]
HashMap = list[MyList|None]

def my_list_create():
    return []

def my_list_put(my_list:MyList, key:str, value:int) -> None:
    # """
    # >>> l = my_list_create()
    # >>> my_list_put(l, "k1", 1)
    # >>> my_list_put(l, "k1", 3)
    # >>> my_list_get(l, "k1")
    # 3
    # """
    my_list_del(my_list, key)
    my_list.append((key, value))
    return

def my_list_get(my_list:MyList, key:str) -> int|None:
    # """
    # >>> l = my_list_create()
    # >>> my_list_put(l, "k1", 1)
    # >>> my_list_get(l, "k1")
    # 1
    # >>> my_list_get(l, "k2")
    # """
    for m_key, value in my_list:
        if m_key == key:
            return value

    return None

def my_list_del(my_list:MyList, key:str) -> None:
    for index, (m_key, _) in enumerate(my_list):
        if m_key == key:
            del my_list[index]
            return

def my_list_each(my_list:MyList, func: Callable[[str, int], None]) -> None:
    # """
    # >>> l = my_list_create()
    # >>> my_list_put(l, "k1", 1)
    # >>> my_list_put(l, "k2", 2)
    # >>> def my_func(key, value) -> None:
    # ...     print(key, value)
    # ...     return
    # >>> my_list_each(l, my_func)
    # k1 1
    # k2 2
    # """
    for m_key, m_value in my_list:
        func(m_key, m_value)

    return

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
    # return [[] for _ in range(256)]
    return []

def hash_map_put(hash_map:HashMap, key:str, value:int) -> None:
    """
    >>> h = hash_map_create()
    >>> hash_map_put(h, "k2", 3)
    >>> hash_map_put(h, "k1", 1)
    >>> hash_map_put(h, "k1", 3)
    >>> hash_map_get(h, "k1")
    3
    """
    index = hash_algorithm(key) % len(hash_map)
    if index >= len(hash_map):
        hash_map.extend([None] * (index - len(hash_map) + 1))
        # hash_map.extend([my_list_create() for _ in range(index - len(hash_map) + 1)])

    if hash_map[index] is None:
        x = hash_map[index] = my_list_create()

    my_list_put(x, key, value)

def hash_map_get(hash_map:HashMap, key:str) -> int|None:
    """
    >>> h = hash_map_create()
    >>> hash_map_put(h, "k1", 1)
    >>> hash_map_get(h, "k1")
    1
    >>> hash_map_get(h, "k2")
    """
    # index = hash_algorithm(key)
    # my_list = hash_map[index]
    # return my_list_get(my_list, key)

    index = hash_algorithm(key) % len(hash_map)

    if index < len(hash_map):
        x = hash_map[index]
        if x is not None:
            return my_list_get(x, key)

    return None

def hash_map_del(hash_map:HashMap, key:str) -> None:
    # index = hash_algorithm(key)
    # my_list = hash_map[index]
    # my_list_del(my_list, key)

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
