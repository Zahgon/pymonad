from typing import TypeVar

import pymonad.monad
import pymonad.operators.operators
import pymonad.writer

T = TypeVar('T') # pylint: disable=invalid-name

class Writer(pymonad.operators.operators.MonadOperators, pymonad.writer.Writer[T]): # pylint: disable=abstract-method
    pass
