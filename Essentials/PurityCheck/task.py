from typing import Callable
from random import randint


class Integer:
    def __init__(self, value: int):
        self.value = value


def increment_fn(input_val: Integer) -> Integer:
    return Integer(input_val.value + 1)


def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:
    """
    increment(input_val) value == increment(input_val) value
    increment(Integer(2)) value == increment(increment(Integer(1))) value
    objects are different (don't point to the same global variable)
    increment(Integer(1)) should return Integer(2)
    """
    input_number = randint(0, 100)
    input_val = Integer(input_number)
    return (increment_fn(input_val).value == increment_fn(input_val).value) \
           and (increment_fn(increment_fn(input_val)).value == increment_fn(Integer(input_number+1)).value) \
           and ((increment_fn(input_val)) != (increment_fn(input_val))) \
           and (increment_fn(input_val).value == Integer(input_number+1).value)


if __name__ == '__main__':
    print(is_pure(increment_fn))
