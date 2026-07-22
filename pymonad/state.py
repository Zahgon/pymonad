
from typing import Any, Callable, Generic, Tuple, TypeVar, Union # pylint: disable=unused-import

import pymonad.monad
import pymonad.tools

A = TypeVar('A') # pylint: disable=invalid-name
B = TypeVar('B') # pylint: disable=invalid-name
S = TypeVar('S') # pylint: disable=invalid-name

@pymonad.tools.curry(3)
def _amap(monad_function, monad_value, state):
    pass

@pymonad.tools.curry(3)
def _bind(monad_value, kleisli_function, state):
    pass

@pymonad.tools.curry(3)
def _bind_or_map(monad_value, function, state):
    pass

@pymonad.tools.curry(3)
def _map(monad_value, function, state):
    pass

class State(pymonad.monad.Monad, Generic[S, A]):
    def __init__(self, state_function, _=None):
        super().__init__(state_function, None)

    @classmethod
    def insert(cls, value: A) -> 'State[Any, A]':
        """ See Monad.insert. """
        return cls(lambda s: (value, s))

    def amap(self: 'State[S, Callable[[A], B]]', monad_value: 'State[S, A]') -> 'State[S, B]':
        pass

    def bind(
            self: 'State[S, A]', kleisli_function: Callable[[A], 'State[S, B]']
    ) -> 'State[S, B]':
        pass

    def map(self: 'State[S, A]', function: Callable[[A], B]) -> 'State[S, B]':
        pass

    def run(self: 'State[S, A]', input_state: S) -> Tuple[A, S]:
        pass

    def then(
            self: 'State[S, A]', function: Union[Callable[[A], B], Callable[[A], 'State[S, B]']]
    ) -> 'State[S, B]':
        pass
