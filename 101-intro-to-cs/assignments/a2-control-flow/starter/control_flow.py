"""Assignment a2: control flow. The test suite is the specification."""


def fizzbuzz(n, rules):
    """Return a list of n strings for the numbers 1..n.

    rules is a list of (divisor, word) pairs, applied in order: words of
    all matching rules are concatenated. Numbers matching no rule appear
    as str(number).

    fizzbuzz(15, [(3, "Fizz"), (5, "Buzz")])[14] == "FizzBuzz"
    """
    raise NotImplementedError


def to_binary(n):
    """Return the binary representation of non-negative n as a string.

    Build it yourself with // and % — bin()/format() are rejected by the
    tests. to_binary(0) == "0".
    """
    raise NotImplementedError


def is_leap_year(year):
    """Gregorian leap year: divisible by 4, except centuries need 400."""
    raise NotImplementedError


def longest_run(items):
    """Return the length of the longest run of equal adjacent items.

    longest_run([1, 1, 2, 2, 2, 3]) == 3; longest_run([]) == 0.
    """
    raise NotImplementedError
