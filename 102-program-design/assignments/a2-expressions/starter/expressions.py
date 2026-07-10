"""Assignment a2: arithmetic expression trees, dispatch only.

The tests reject isinstance, type(), and match statements in this module.
Composite nodes must talk to children through evaluate/render/variables.
"""


class Literal:
    """A constant. Literal(2).evaluate({}) == 2; render() == "2"."""

    def __init__(self, value):
        raise NotImplementedError

    def evaluate(self, env):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def variables(self):
        raise NotImplementedError


class Var:
    """A named variable, looked up in env at evaluation time.

    Var("x").evaluate({"x": 5}) == 5.
    Missing name -> NameError mentioning the name. render() == the name.
    """

    def __init__(self, name):
        raise NotImplementedError

    def evaluate(self, env):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def variables(self):
        raise NotImplementedError


class Add:
    """Sum of two subexpressions. render() == "(L + R)"."""

    def __init__(self, left, right):
        raise NotImplementedError

    def evaluate(self, env):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def variables(self):
        raise NotImplementedError


class Mul:
    """Product of two subexpressions. render() == "(L * R)"."""

    def __init__(self, left, right):
        raise NotImplementedError

    def evaluate(self, env):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def variables(self):
        raise NotImplementedError


class Neg:
    """Negation of one subexpression. render() == "(-X)"."""

    def __init__(self, inner):
        raise NotImplementedError

    def evaluate(self, env):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def variables(self):
        raise NotImplementedError
