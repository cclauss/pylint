"""Regression tests for inferred.qname missing"""

# pylint: disable=missing-docstring,too-few-public-methods,disallowed-name

X = slice(42)
X()  # [not-callable]


class Foo:
    def __init__(self, foo=slice(42)):
        self.foo = foo


def bar():
    i = Foo()
    i.foo()
    return 100
