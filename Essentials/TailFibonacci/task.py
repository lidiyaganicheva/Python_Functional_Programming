from typing import Callable

from Essentials.Factorial.tail_recursion import tail_call_optimized


@tail_call_optimized
def fibonacci_impl(x: int, curr: int = 1, next: int = 1) -> Callable[[int], int]:
    """
    x - number to count
    curr - fibonacci number for this iteration
    next - number to add to get curr for the next iteration
    """
    if x == 1:
        return curr
    if x == 0:
        return x
    return fibonacci_impl(x - 1, next, curr + next)


if __name__ == '__main__':
    print(fibonacci_impl(10, 1, 1))
