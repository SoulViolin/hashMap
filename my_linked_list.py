from typing import Callable
from dataclasses import dataclass

@dataclass
class MyList:
    value: tuple[str, int]
    next: 'MyList|None'

def my_list_put(my_list:MyList|None, key:str, value:int) -> MyList:
    """
    >>> l = my_list_put(None, "k1", 1)
    >>> l = my_list_put(l, "k1", 3)
    >>> my_list_get(l, "k1")
    3
    """
    head = my_list

    if my_list is None:
        return MyList((key, value), None)

    while head is not None:
        m_key, _ = head.value

        if m_key == key:
            head.value = (m_key, value)

            return my_list

        head = head.next

    return MyList((key, value), my_list)

def my_list_get(my_list:MyList|None, key:str) -> int|None:
    """
    >>> l = my_list_put(None, "k1", 1)
    >>> my_list_get(l, "k1")
    1
    >>> my_list_get(l, "k2")
    """
    head = my_list

    while head is not None:
        m_key, m_value = head.value

        if m_key == key:
            return m_value

        head = head.next

def my_list_del(my_list:MyList|None, key:str) -> MyList|None:
    if my_list is None:
        return None

    head = my_list
    last = None

    while head is not None:
        m_key, _ = head.value

        if m_key == key:
            if last is not None:
                last.next = head.next

                return my_list
            else:
                return head.next

        last = head
        head = head.next

def my_list_each(my_list:MyList|None, func: Callable[[str, int], None]) -> None:
    """
    >>> l = my_list_put(None, "k1", 1)
    >>> l = my_list_put(l, "k2", 2)
    >>> def my_func(key, value) -> None:
    ...     print(key, value)
    ...     return
    >>> my_list_each(l, my_func)
    k2 2
    k1 1
    """
    head = my_list

    while head is not None:
        m_key, m_value = head.value
        func(m_key, m_value)

        head = head.next
