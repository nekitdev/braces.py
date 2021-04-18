import token as TOKEN

__all__ = ("EXCEPT", "INDENT", "LINE_LENGTH", "TOKEN")

LINE_LENGTH = 100  # line length to use while formatting code

TOKEN.COLONEQUAL = 0xFF  # for versions that have assignment expressions implemented

SPACE = " "

INDENT_LENGTH = 4  # length of indentation to use
INDENT = SPACE * INDENT_LENGTH  # actual string to apply as one indent

NEWLINES = {TOKEN.NEWLINE, TOKEN.NL}  # tokens that are considered as newlines

EXCEPT = {  # symbols after which we do not expect to have {...} used for indentation
    TOKEN.NEWLINE,  # \n
    TOKEN.NL,  # \n
    TOKEN.LPAR,  # (
    TOKEN.LSQB,  # [
    TOKEN.COLON,  # :
    TOKEN.COMMA,  # ,
    TOKEN.SEMI,  # ;
    TOKEN.PLUS,  # +
    TOKEN.MINUS,  # -
    TOKEN.STAR,  # *
    TOKEN.SLASH,  # /
    TOKEN.VBAR,  # |
    TOKEN.AMPER,  # &
    TOKEN.LESS,  # <
    TOKEN.GREATER,  # >
    TOKEN.EQUAL,  # =
    TOKEN.DOT,  # .
    TOKEN.PERCENT,  # %
    TOKEN.LBRACE,  # {
    TOKEN.EQEQUAL,  # ==
    TOKEN.NOTEQUAL,  # !=
    TOKEN.LESSEQUAL,  # <=
    TOKEN.GREATEREQUAL,  # >=
    TOKEN.TILDE,  # ~
    TOKEN.CIRCUMFLEX,  # ^
    TOKEN.LEFTSHIFT,  # <<
    TOKEN.RIGHTSHIFT,  # >>
    TOKEN.DOUBLESTAR,  # **
    TOKEN.PLUSEQUAL,  # +=
    TOKEN.MINEQUAL,  # -=
    TOKEN.STAREQUAL,  # *=
    TOKEN.SLASHEQUAL,  # /=
    TOKEN.PERCENTEQUAL,  # %=
    TOKEN.AMPEREQUAL,  # &=
    TOKEN.VBAREQUAL,  # |=
    TOKEN.CIRCUMFLEXEQUAL,  # ^=
    TOKEN.LEFTSHIFTEQUAL,  # <<=
    TOKEN.RIGHTSHIFTEQUAL,  # >>=
    TOKEN.DOUBLESTAREQUAL,  # **=
    TOKEN.DOUBLESLASH,  # //
    TOKEN.DOUBLESLASHEQUAL,  # //=
    TOKEN.AT,  # @
    TOKEN.ATEQUAL,  # @=
    TOKEN.RARROW,  # ->
    TOKEN.COLONEQUAL,  # :=
}
