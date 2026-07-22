from typing import Callable, TypeVar

import pymonad.monad
import pymonad.operators.operators
import pymonad.io

T = TypeVar('T') # pylint: disable=invalid-name

class _IO(pymonad.operators.operators.MonadOperators, pymonad.io._IO[T]): # pylint: disable=protected-access, abstract-method
    pass

def IO(io_function: Callable[[], T]) -> _IO[T]: # pylint: disable=invalid-name
    pass

IO.apply = _IO.apply
IO.insert = _IO.insert
