import token as TOKEN

__all__ = ('EXCEPT', 'INDENT', 'NEWLINE', 'TOKEN')

TOKEN.COLONEQUAL = 0xff  # for 3.8 onward

INDENT = ' ' * 4

NEWLINE = {TOKEN.NEWLINE, TOKEN.NL}

EXCEPT = {
    TOKEN.NEWLINE,           # \n
    TOKEN.NL,                # \n
    TOKEN.LPAR,              # (
    TOKEN.LSQB,              # [
    TOKEN.COLON,             # :
    TOKEN.COMMA,             # ,
    TOKEN.SEMI,              # ;
    TOKEN.PLUS,              # +
    TOKEN.MINUS,             # -
    TOKEN.STAR,              # *
    TOKEN.SLASH,             # /
    TOKEN.VBAR,              # |
    TOKEN.AMPER,             # &
    TOKEN.LESS,              # <
    TOKEN.GREATER,           # >
    TOKEN.EQUAL,             # =
    TOKEN.DOT,               # .
    TOKEN.PERCENT,           # %
    TOKEN.LBRACE,            # {
    TOKEN.EQEQUAL,           # ==
    TOKEN.NOTEQUAL,          # !=
    TOKEN.LESSEQUAL,         # <=
    TOKEN.GREATEREQUAL,      # >=
    TOKEN.TILDE,             # ~
    TOKEN.CIRCUMFLEX,        # ^
    TOKEN.LEFTSHIFT,         # <<
    TOKEN.RIGHTSHIFT,        # >>
    TOKEN.DOUBLESTAR,        # **
    TOKEN.PLUSEQUAL,         # +=
    TOKEN.MINEQUAL,          # -=
    TOKEN.STAREQUAL,         # *=
    TOKEN.SLASHEQUAL,        # /=
    TOKEN.PERCENTEQUAL,      # %=
    TOKEN.AMPEREQUAL,        # &=
    TOKEN.VBAREQUAL,         # |=
    TOKEN.CIRCUMFLEXEQUAL,   # ^=
    TOKEN.LEFTSHIFTEQUAL,    # <<=
    TOKEN.RIGHTSHIFTEQUAL,   # >>=
    TOKEN.DOUBLESTAREQUAL,   # **=
    TOKEN.DOUBLESLASH,       # //
    TOKEN.DOUBLESLASHEQUAL,  # //=
    TOKEN.AT,                # @
    TOKEN.ATEQUAL,           # @=
    TOKEN.RARROW,            # ->
    TOKEN.COLONEQUAL,        # :=
}
