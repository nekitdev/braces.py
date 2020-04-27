import codecs
from encodings import utf_8
from io import StringIO
from typing import Any, Optional, Tuple, Union

from .token_transform import transform

__all__ = ("decode",)


def decode(source: Union[bytes, memoryview], errors: str = "strict") -> str:
    if isinstance(source, memoryview):
        source = source.tobytes()
    return transform(source.decode("utf-8")).rstrip()


def braces_decode(
    source: Union[bytes, memoryview], errors: str = "strict"
) -> Tuple[str, int]:
    return decode(source), len(source)


def transform_stream(stream: Any) -> StringIO:
    return StringIO(transform(stream.read()))


class BracesIncrementalDecoder(utf_8.IncrementalDecoder):
    def decode(self, input_bytes: bytes, final: bool = False) -> str:
        self.buffer += input_bytes

        if final and self.buffer:
            buffer = self.buffer
            self.buffer = bytes()

            result = super().decode(
                decode(buffer).encode("utf-8"), final=True
            )
            return result

        else:
            return ""


class BracesStreamReader(utf_8.StreamReader):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.stream = transform_stream(self.stream)  # type: StringIO


def search_function(encoding: str) -> Optional[codecs.CodecInfo]:
    if encoding != "braces":
        return None  # propagate

    # assume utf-8 encoding
    return codecs.CodecInfo(
        name="braces",
        encode=utf_8.encode,  # type: ignore
        decode=braces_decode,  # type: ignore
        incrementalencoder=utf_8.IncrementalEncoder,
        incrementaldecoder=BracesIncrementalDecoder,
        streamreader=utf_8.StreamReader,
        streamwriter=BracesStreamReader,
    )


codecs.register(search_function)
