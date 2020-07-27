"""Library that implements braces for Python Programming Language."""

__title__ = "braces"
__author__ = "NeKitDS"
__copyright__ = "Copyright 2020 NeKitDS"
__license__ = "MIT"
__version__ = "0.1.3"

from collections import namedtuple
import re
import token
from typing import cast

from .const import EXCEPT, TOKEN
from .register_codec import decode
from .token_transform import SmallToken, test_compile, transform


VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")

_normal_re = (
    r"^\s*(?:"
    r"(?P<major>\d+)"
    r"(?P<split>[\.-])?"
    r"(?P<minor>\d+)?"
    r"(?P=split)?"
    r"(?P<micro>\d+)?"
    r"(?P<releaselevel>a|b|rc|f|dev)?"
    r"(?P<serial>\d+)?"
    r")\s*$"
)
_compiled_re = re.compile(_normal_re, re.MULTILINE)


def make_version_details(ver: str) -> VersionInfo:
    match = _compiled_re.match(ver)

    if match is None:
        return VersionInfo(0, 0, 0, "final", 0)

    args = {}

    for key, value in match.groupdict().items():
        if key == "split":
            continue

        elif key == "releaselevel":
            if value is None:
                value = "f"

            value = {
                "a": "alpha",
                "b": "beta",
                "rc": "candidate",
                "f": "final",
                "dev": "developer",
            }.get(value, "final")

        elif value is None or not value.isdigit():
            value = 0  # type: ignore

        else:
            value = int(value)  # type: ignore

        args[key] = value

    return VersionInfo(**args)


version_info = make_version_details(__version__)


del namedtuple, re
