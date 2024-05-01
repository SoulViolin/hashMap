from typing import Callable

MyList = list[tuple[str, int]]

def my_list_create():
    return []

def my_list_put(my_list:MyList, key:str, value:int) -> None:
    """
    >>> l = my_list_create()
    >>> my_list_put(l, "k1", 1)
    >>> my_list_put(l, "k1", 3)
    >>> my_list_get(l, "k1")
    3
    """
    my_list_del(my_list, key)
    my_list.append((key, value))
    return

def my_list_get(my_list:MyList, key:str) -> int|None:
    """
    >>> l = my_list_create()
    >>> my_list_put(l, "k1", 1)
    >>> my_list_get(l, "k1")
    1
    >>> my_list_get(l, "k2")
    """
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
    """
    >>> l = my_list_create()
    >>> my_list_put(l, "k1", 1)
    >>> my_list_put(l, "k2", 2)
    >>> def my_func(key, value) -> None:
    ...     print(key, value)
    ...     return
    >>> my_list_each(l, my_func)
    k1 1
    k2 2
    """
    for m_key, m_value in my_list:
        func(m_key, m_value)

    return
