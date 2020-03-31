import codecs
from encodings import utf_8
from io import StringIO
from typing import Any, Optional

from .token_transform import transform

__all__ = ('decode',)


def decode(input_bytes: bytes, errors: str = 'strict') -> str:
    return transform(input_bytes.decode('utf-8')).rstrip()


def braces_decode(input_bytes: bytes, errors: str = 'strict') -> str:
    return decode(input_bytes), len(input_bytes)


def transform_stream(stream: Any) -> StringIO:
    return StringIO(transform(stream.read()))


class BracesIncrementalDecoder(utf_8.IncrementalDecoder):
    def decode(self, input_bytes: bytes, final: bool = False) -> str:
        self.buffer += input_bytes

        if final:
            buffer = self.buffer
            self.buffer = bytes()

            return super(type(self), self).decode(decode(buffer).encode('utf-8'), final=True)

        else:
            return ''


class BracesStreamReader(utf_8.StreamReader):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.stream = transform_stream(self.stream)


def search_function(encoding: str) -> Optional[codecs.CodecInfo]:
    if encoding != 'braces':
        return None  # propagate

    # assume utf-8 encoding
    return codecs.CodecInfo(
        name='braces',
        encode=utf_8.encode,
        decode=decode,
        incrementalencoder=utf_8.IncrementalEncoder,
        incrementaldecoder=BracesIncrementalDecoder,
        streamreader=BracesStreamReader,
        streamwriter=utf_8.StreamWriter
    )


codecs.register(search_function)
