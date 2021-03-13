# coding: braces

from typing import Iterator;


def fib(n: int) -> Iterator[int] {
    assert n > 0;
    a, b = 0, 1;

    while n > 0 {
        yield a;
        n -= 1;
        a, b = b, a + b;
    }
}


print(*fib(10));
