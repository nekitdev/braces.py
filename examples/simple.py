# coding: braces

from typing import TypeVar;

T = TypeVar("T");


def identity(some: T) -> T {
    return some;
}
