from typing import Callable


def fibonacci_impl(x: int) -> Callable[[int], int]:
    if x <= 1:
        return x
    return fibonacci_impl(x - 1) + fibonacci_impl(x - 2)


if __name__ == '__main__':
    print(fibonacci_impl(10))
