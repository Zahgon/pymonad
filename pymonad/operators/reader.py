from typing import Callable, TypeVar

import pymonad.monad
import pymonad.operators.operators
import pymonad.reader

R = TypeVar('R') # pylint: disable=invalid-name
T = TypeVar('T') # pylint: disable=invalid-name

class _Reader(pymonad.operators.operators.MonadOperators, pymonad.reader._Reader[R, T]): # pylint: disable=protected-access, abstract-method
    pass

def Reader(function: Callable[[R], T]) -> _Reader[R, T]: # pylint: disable=invalid-name
    pass

Reader.apply = _Reader.apply
Reader.insert = _Reader.insert
