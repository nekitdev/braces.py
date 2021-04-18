import codecs
import encodings
from io import StringIO
from typing import Any, Optional, Tuple, TypeVar

from braces.transform import transform

__all__ = ("decode", "encode")

BRACES = "braces"

EMPTY = ""

UTF_8 = "utf-8"
STRICT = "strict"

B = TypeVar("B", bytes, bytearray, memoryview)

utf_8 = encodings.search_function(UTF_8)


def decode(
    source: B, encoding: str = UTF_8, errors: str = STRICT, **transform_args: Any
) -> str:
    return transform(bytes(source).decode(encoding, errors), **transform_args)


def encode(
    source: B,
    encoding: str = UTF_8,
    errors: str = STRICT,
    **transform_back_args: Any
) -> str:
    ...


def braces_decode(source: B, errors: str = STRICT) -> Tuple[str, int]:
    code, length = utf_8.decode(source, errors)

    return transform(code, add_lines=True), length


def transform_stream(stream: Any) -> StringIO:
    return StringIO(transform(stream.read(), add_lines=True))


class BracesIncrementalDecoder(codecs.BufferedIncrementalDecoder):
    def _buffer_decode(
        self, input: B, errors: str = STRICT, final: bool = False
    ) -> Tuple[str, int]:
        if final:
            return braces_decode(input, errors)

        else:
            return EMPTY, 0


class BracesStreamReader(utf_8.streamreader):  # type: ignore
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.stream: StringIO = transform_stream(self.stream)


def search_function(encoding: str) -> Optional[codecs.CodecInfo]:
    if encoding != BRACES:
        return None  # propagate

    # assume utf-8 encoding
    return codecs.CodecInfo(
        name=BRACES,
        encode=utf_8.encode,
        decode=braces_decode,  # type: ignore
        incrementalencoder=utf_8.incrementalencoder,
        incrementaldecoder=BracesIncrementalDecoder,
        streamreader=BracesStreamReader,
        streamwriter=utf_8.streamwriter,
    )


codecs.register(search_function)
