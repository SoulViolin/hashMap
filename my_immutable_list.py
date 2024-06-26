from typing import Callable

type MyList[X] = tuple[X, MyList[X]|None]

def my_list_head[X](my_list:MyList[X]|None) -> X|None:
    """
    >>> my_list_head((1, (2, None)))
    1
    >>> my_list_head(None)
    """
    if my_list is None:
        return None

    head, _tail = my_list
    return head

def my_list_tail(my_list:MyList|None) -> MyList|None:
    """
    >>> my_list_tail((1, (2, None)))
    (2, None)
    >>> my_list_tail(None)
    """
    if my_list is None:
        return None

    _head, tail = my_list
    return tail

def my_list_len(my_list:MyList|None) -> int:
    """
    >>> my_list_len((1, (2, (3, None))))
    3
    >>> my_list_len(None)
    0
    """
    len = 0

    while my_list is not None:
        _head, my_list = my_list

        len += 1

    return len

def my_list_len_rec(my_list:MyList|None) -> int:
    """
    >>> my_list_len_rec((1, (2, (3, None))))
    3
    >>> my_list_len_rec(None)
    0
    """
    if my_list is None:
        return 0

    _head, tail = my_list

    return 1 + my_list_len_rec(tail)

def my_list_prepend(my_list:MyList|None, value) -> MyList:
    """
    >>> my_list_prepend((1, (2, None)), 0)
    (0, (1, (2, None)))
    >>> my_list_prepend(None, 0)
    (0, None)
    """
    return (value, my_list)

def my_list_reverse_rec(my_list: MyList|None, other_list: MyList|None = None) -> MyList|None:
    """
    >>> my_list_reverse_rec((1, (2, None)))
    (2, (1, None))
    >>> my_list_reverse_rec(None)
    """
    if my_list is None:
        return other_list

    head, tail = my_list
    return my_list_reverse_rec(tail, (head, other_list))

def my_list_reverse(my_list: MyList|None) -> MyList|None:
    """
    >>> my_list_reverse((1, (2, None)))
    (2, (1, None))
    >>> my_list_reverse(None)
    """
    new_list = None

    while my_list is not None:
        head, my_list = my_list

        new_list = (head, new_list)

    return new_list

def my_list_append(my_list: MyList|None, value) -> MyList|None:
    """
    >>> my_list_append((1, (2, None)), 3)
    (1, (2, (3, None)))
    >>> my_list_append(None, 3)
    (3, None)
    """
    return my_list_reverse(my_list_prepend(my_list_reverse(my_list), value))

def my_list_each[X](my_list: MyList[X]|None, func: Callable[[X], None]) -> None:
    """
    >>> my_list_each((1, (2, None)), print)
    1
    2
    >>> my_list_each(None, print)
    """
    while my_list is not None:
        head, my_list = my_list
        func(head)

def my_list_del[X](my_list: MyList[X]|None, func: Callable[[X], bool]) -> MyList[X]|None:
    """
    >>> my_list_del((1, (2, None)), lambda x: x == 2)
    (1, None)
    >>> my_list_del((1, (2, None)), lambda x: True)
    """
    new_list = None

    while my_list is not None:
        head, my_list = my_list
        if not func(head):
            new_list = (head, new_list)

    return my_list_reverse(new_list)

def my_list_find[X](my_list: MyList[X]|None, func: Callable[[X], bool]) -> X|None:
    """
    >>> my_list_find((1, (2, None)), lambda x: x == 2)
    2
    >>> my_list_find((1, (2, None)), lambda x: True)
    1
    >>> my_list_find((1, (2, None)), lambda x: False)
    """
    while my_list is not None:
        head, my_list = my_list
        if func(head):
            return head
