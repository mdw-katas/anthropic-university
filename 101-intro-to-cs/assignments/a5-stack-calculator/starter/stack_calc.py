"""Assignment a5: a stack and two classic uses. Tests are the spec."""


class Stack:
    """A LIFO stack. pop/peek on empty raise IndexError."""

    def __init__(self):
        raise NotImplementedError

    def push(self, value):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def size(self):
        raise NotImplementedError


def tokenize(expression):
    """Split an expression on whitespace: "3 4 +" -> ["3", "4", "+"]."""
    raise NotImplementedError


def evaluate_rpn(tokens):
    """Evaluate Reverse Polish Notation supporting + - * /.

    Operands push onto a stack; each operator pops two (first pop is the
    RIGHT operand), applies, pushes the result. Numbers may be negative
    or fractional — float(token) is your friend. Malformed input raises
    ValueError.
    """
    raise NotImplementedError


def balanced(text):
    """Return True iff every ( [ { closes correctly with ) ] }.

    All other characters are ignored. Use your Stack.
    """
    raise NotImplementedError
