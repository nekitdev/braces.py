# coding: braces

from typing import List, Union;

def fizzbuzz(n: int) -> List[Union[int, str]] {
    assert n > 0;
    result = [];
    for x in range(n) {
        buffer = '';
        if not x % 3 {
            buffer += 'fizz';
        } if not x % 5 {
            buffer += 'buzz';
        }
        result.append(buffer if buffer else x);
    }
    return result;
}

print(*fizzbuzz(100));
