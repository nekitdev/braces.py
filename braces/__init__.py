"""Library that implements braces for Python Programming Language."""

__title__ = "braces"
__author__ = "nekitdev"
__copyright__ = "Copyright 2020-2021 nekitdev"
__license__ = "MIT"
__version__ = "0.2.0"

from braces.constants import EXCEPT, LINE_LENGTH, TOKEN  # noqa
from braces.encoding import decode, encode  # noqa
from braces.transform import transform, transform_back  # noqa
