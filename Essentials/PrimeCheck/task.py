from Essentials.Factorial.tail_recursion import tail_call_optimized


@tail_call_optimized
def is_prime(n: int, i: int = 1, result: bool = False) -> bool:
    """n - number to check. n-1 = maximum depth of recursion
    i - divider.
    result - result of division. If reminder = 0 then number is non-prime"""
    if (i < n) & (result is True):
        return False
    if i == n:
        return True
    return is_prime(n, i+1, n % (i+1) == 0)


if __name__ == '__main__':
    print(is_prime(5, 1, False))

