# coding: braces

from typing import Generator;

def fib(n: int) -> Generator[int, None, None] {
    assert n > 0;
    a, b = 0, 1;

    while n > 0 {
        yield a;
        n -= 1;
        a, b = b, a + b;
    }
}

print(*fib(10));
