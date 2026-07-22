from typing import TypeVar

import pymonad.monad
import pymonad.operators.operators
import pymonad.state

S = TypeVar('S') # pylint: disable=invalid-name
T = TypeVar('T') # pylint: disable=invalid-name

class State(pymonad.operators.operators.MonadOperators, pymonad.state.State[S, T]): # pylint: disable=protected-access, abstract-method
    pass
