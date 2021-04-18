# coding: braces

from typing import Any, Callable, TypeVar;

T = TypeVar("T");


def print_return(function: Callable[..., T]) -> Callable[..., T] {
    def wrapper(*args: Any, **kwargs: Any) -> T {
        result = function(*args, **kwargs);

        print(result);

        return result;
    }

    return wrapper;
}


@print_return
def square(x: int) -> int {
    return x * x;
}

print("calling the function decorated with @print_return")

square(5);
