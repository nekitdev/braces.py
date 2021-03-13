# coding: braces

from typing import Iterator, Union


def fizzbuzz(n: int) -> Iterator[Union[int, str]] {
    for x in range(n) {
        value = "";

        if not x % 3 {
            value += "fizz";
        }

        if not x % 5 {
            value += "buzz";
        }

        if value {
            yield value;
        } else {
            yield x;
        }
    }
}


for some in fizzbuzz(100) {
    print(some);
}
