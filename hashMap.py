from typing import Callable

HashMap = list[tuple[str, int]]

def hash_map_create():
    return []

def hash_map_put(hash_map:HashMap, key:str, value:int) -> None:
    hash_map_del(hash_map, key)
    hash_map.append((key, value))
    return

def hash_map_get(hash_map:HashMap, key:str) -> int|None:
    for m_key, value in hash_map:
        if m_key == key:
            return value

    return None

def hash_map_del(hash_map:HashMap, key:str) -> None:
    for index, (m_key, _) in enumerate(hash_map):
        if m_key == key:
            del hash_map[index]
            return

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
    for m_key, m_value in hash_map:
        func(m_key, m_value)

    return

