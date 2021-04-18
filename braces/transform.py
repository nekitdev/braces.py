from io import StringIO
from keyword import iskeyword
from tokenize import TokenInfo
from typing import Iterable, Iterator, Tuple, cast
import tokenize

import black

from braces.constants import EXCEPT, INDENT, LINE_LENGTH, NEWLINES, TOKEN

__all__ = (
    "from_tokens",
    "into_tokens",
    "from_real_tokens",
    "into_real_tokens",
    "transform",
    "transform_back",
)

# alright, so we are using a not-really-documented feature
# from tokenize module here; basically, we can pass (type, value)
# pairs instead of tokens that handle their position and so on;
# we are going to get quite a messy output, but this can be easily
# solved via applying some nifty formatter to the result we get.

EMPTY = ""

COLON = ":"

SPACE = " "

LBRACE = "{"
RBRACE = "}"

NEWLINE = "\n"


class Token:
    def __init__(self, type: int, value: str) -> None:
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.type}, {self.value!r})"

    def as_tuple(self) -> Tuple[int, str]:
        return (self.type, self.value)


def into_real_tokens(code: str) -> Iterator[TokenInfo]:
    return tokenize.generate_tokens(StringIO(code).readline)


def from_real_tokens(tokens: Iterable[TokenInfo]) -> str:
    return cast(str, tokenize.untokenize(tokens))


def into_tokens(code: str) -> Iterator[Token]:
    for token in into_real_tokens(code):
        yield Token(token.exact_type, token.string)


def from_tokens(tokens: Iterable[Token]) -> str:
    return cast(str, tokenize.untokenize(token.as_tuple() for token in tokens))


NOT_SET = -1


class Context:
    def __init__(self, start: int = NOT_SET, end: int = NOT_SET) -> None:
        self.start = start
        self.end = end

    @property
    def set(self) -> bool:
        return self.start >= 0 and self.end >= 0


def get_context(start: int = NOT_SET, end: int = NOT_SET) -> Context:
    return Context(start, end)


ALLOWED_KEYWORDS = {
    "False",
    "True",
    "None",
    "else",
    "except",
    "finally",
    "lambda",
    "try",
}


def is_keyword(string: str) -> bool:
    return iskeyword(string) and string not in ALLOWED_KEYWORDS


def transform(code: str, add_lines: bool = False) -> str:
    # we are creating the list here as we need to mutate tokens
    tokens = list(into_tokens(code))

    braces = []

    previous = None

    level = 0

    # stage 1: distinguish between braces in code and dictionaries or sets

    for token in tokens:
        if token.type == TOKEN.LBRACE:  # {
            if (
                not previous
                or previous.type in EXCEPT
                or is_keyword(previous.value)
            ):
                level += 1

            else:
                braces.append(token)

        if token.type == TOKEN.RBRACE:  # }
            if level:
                level -= 1

            else:
                braces.append(token)

        previous = token

    contexts = []

    # stage 2: find matching braces

    for token in braces:
        if token.type == TOKEN.LBRACE:  # {
            contexts.append(get_context(tokens.index(token)))

        else:
            for context in reversed(contexts):
                if not context.set:
                    context.end = tokens.index(token)
                    break

            else:
                raise SyntaxError("Unmatched braces found.")

    offset = 0

    # stage 3: replace braces with appropriate syntax

    for indent, context in enumerate(contexts, 1):
        # get values from the context
        start = context.start
        end = context.end

        # replace "{" with ":"
        token = tokens[start + offset]

        token.type = TOKEN.COLON
        token.value = COLON

        # look ahead if next token is "\n" and add if it is not
        offset += 1

        token = tokens[start + offset]

        if token.type in NEWLINES:
            offset -= 1

        else:
            tokens.insert(start + offset, Token(TOKEN.NL, NEWLINE))

        # replace "}" with dedent
        token = tokens[end + offset]

        token.type = TOKEN.DEDENT
        token.value = EMPTY

        # insert an indent
        offset += 1

        tokens.insert(start + offset, Token(TOKEN.INDENT, INDENT * indent))

    offset = 0

    # stage 4: find and remove unused semicolons, adding newlines if needed

    for index, token in enumerate(tokens.copy()):  # copying because we are going to modify tokens
        if token.type == TOKEN.SEMI:
            next = tokens[index - offset + 1]

            if next.type in NEWLINES:
                tokens.pop(index - offset)
                offset += 1

            else:
                token.type = TOKEN.NL
                token.value = NEWLINE

    # stage 5: create code from tokens and format it

    code = from_tokens(tokens)

    lines = len(code) - len(code.lstrip(NEWLINE)) if add_lines else 0

    code = NEWLINE * lines + black.format_str(
        code, mode=black.FileMode(line_length=LINE_LENGTH)
    )

    return code


def transform_back(code: str, semicolons: bool = True) -> str:
    ...  # TODO: implement this, obviously, when one has time to devote into this library
