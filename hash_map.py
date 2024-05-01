from typing import Callable
from my_immutable_list import MyList, my_list_append, my_list_del, my_list_each, my_list_find

HashMap = list[MyList[tuple[str, int]]|None]

def hash_algorithm(s) -> int:
    current_value = 0

    for char in s:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256

    return current_value

def hash_map_create():
    return [None for _ in range(8)]

def my_list_del_str(my_list:MyList|None, key:str) -> MyList|None:
    def func(t:tuple[str, int]) -> bool:
        m_key, _value = t
        return m_key == key

    return my_list_del(my_list, func)

def my_list_put(my_list:MyList|None, key:str, value:int) -> MyList|None:
    return my_list_append(my_list_del_str(my_list, key), (key, value))

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
    hash_map[index] = my_list_put(hash_map[index], key, value)

def my_list_get(my_list:MyList|None, key:str) -> int|None:
    def func(t:tuple[str, int]) -> bool:
        m_key, _value = t
        return m_key == key

    result = my_list_find(my_list, func)
    if result is None:
        return None

    return result[1]

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

    hash_map[index] = my_list_del_str(hash_map[index], key)

def hash_map_each(hash_map:HashMap, func: Callable[[tuple[str, int]], None]) -> None:
    """
    >>> h = hash_map_create()
    >>> hash_map_put(h, "k1", 1)
    >>> hash_map_put(h, "k2", 2)
    >>> def func(t):
    ...    print(t[0], t[1])
    >>> hash_map_each(h, func)
    k1 1
    k2 2
    """
    for my_list in hash_map:
        if my_list is not None:
            my_list_each(my_list, func)
