from collections import namedtuple
from io import StringIO
import tokenize

import black  # type: ignore  # does not see type hints

from .const import EXCEPT, INDENT, NEWLINE, TOKEN

__all__ = ("test_compile", "transform", "SmallToken")

SmallToken = namedtuple("SmallToken", "type string")


def test_compile(code: str) -> None:
    compile(code, "<test>", "exec")


def transform(code: str) -> str:
    tokens = list(tokenize.generate_tokens(StringIO(code).readline))

    result = [SmallToken(token.exact_type, token.string) for token in tokens]

    braces = []
    in_dict_or_set = False
    previous = None

    for token in tokens:
        if token.exact_type == TOKEN.LBRACE:
            if not previous or previous.exact_type in EXCEPT:
                in_dict_or_set = True
            else:
                braces.append(token)
        if token.exact_type == TOKEN.RBRACE:
            if in_dict_or_set:
                in_dict_or_set = False
            else:
                braces.append(token)
        previous = token

    contexts = []

    # go through brace tokens and find pairs using context method
    for token in braces:
        if token.exact_type == TOKEN.LBRACE:
            contexts.append([tokens.index(token), -1])
        else:
            for context in reversed(contexts):
                if context[1] == -1:
                    context[1] = tokens.index(token)
                    break
            else:
                raise SyntaxError("Unmatched braces found.")

    offset = 0

    # replace braces with ':' and indents
    for indent, (start, end) in enumerate(contexts, 1):

        # replace '{' with ':'
        result[start + offset] = SmallToken(TOKEN.COLON, ":")

        # look if next is '\n' and add newline if it is not
        offset += 1
        if result[start + offset].type in NEWLINE:
            offset -= 1
        else:
            result.insert(start + offset, SmallToken(TOKEN.NL, "\n"))

        # replace '}' with dedent
        result[end + offset] = SmallToken(TOKEN.DEDENT, "")

        # add indent
        offset += 1
        result.insert(start + offset, SmallToken(TOKEN.INDENT, INDENT * indent))

    offset = 0

    for index, small_token in enumerate(result.copy()):
        # find and remove unused ';', adding newlines if needed
        if small_token.string == ";":
            if result[index - offset + 1].type in NEWLINE:
                result.pop(index - offset)
                offset += 1
            else:
                result[index - offset] = SmallToken(TOKEN.NL, "\n")

    final = tokenize.untokenize(result)

    final = black.format_str(final, mode=black.FileMode(line_length=100))

    return final
