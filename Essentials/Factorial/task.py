from typing import Callable

from Essentials.Factorial.tail_recursion import tail_call_optimized


@tail_call_optimized
def factorial_impl(x: int, result: int = 1) -> Callable[[int], int]:
    """
    x - number to get factorial
    x-2 = depth of recursion
    result - product of consequent numbers started from the highest number (e.g 5*4*3*2*1)
    """
    if x <= 1:
        return result
    return factorial_impl(x-1, x * result)


if __name__ == '__main__':
    print(factorial_impl(5, 1))
