"""Exploration: trust the contract.

Do NOT trace all the way down. Assume reverse works for the smaller
string, and ask what the top-level call assembles. Predict, run, then:
uni grade 101/explore-05
"""

PREDICT_REVERSED = None  # reverse("stack")


def reverse(s):
    if s == "":
        return ""
    return reverse(s[1:]) + s[0]


if __name__ == "__main__":
    print(f'reverse("stack") = {reverse("stack")!r}')
