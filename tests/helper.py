
import unittest
import os


SKIP_INTENTIONAL_FAILS = os.environ.get('SKIP_IFT', False)


def _id(obj):
    return obj


# Tests annotated with this will not run in CI
def skip_intentionally_failing():
    """
    In class I will say 'dont commit code that breaks tests'. This is true. For the lecture code there are examples
    where as part of labs the code is broken and people need to fix. However, I want to run CI on the codebase to
    make sure it is not broken. Therefore, I have added a decorator for tests which I *know* are broken on commit
    so they do not run as part of CI.
    :return:
    """
    if SKIP_INTENTIONAL_FAILS:
        return unittest.skip("Skipping Test")
    return _id
