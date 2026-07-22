
from typing import Any, Callable, Generic, Tuple, TypeVar, Union # pylint: disable=unused-import

import pymonad.monad

A = TypeVar('A') # pylint: disable=invalid-name
B = TypeVar('B') # pylint: disable=invalid-name

def _bind_or_map(monad_value, function):
    pass

class _IO(pymonad.monad.Monad, Generic[A]):
    @classmethod
    def insert(cls, value: A) -> '_IO[A]':
        """ See Monad.insert. """
        return cls(lambda: value, None)

    def amap(self: '_IO[Callable[[A], B]]', monad_value: '_IO[A]') -> '_IO[B]':
        pass

    def bind(self: '_IO[A]', kleisli_function: Callable[[A], '_IO[B]']) -> '_IO[B]':
        pass

    def map(self: '_IO[A]', function: Callable[[A], B]) -> '_IO[B]':
        pass

    def run(self: '_IO[A]') -> A:
        pass

    def then(
            self: '_IO[A]', function: Union[Callable[[A], B], Callable[[A], '_IO[B]']]
    ) -> '_IO[B]':
        pass

def IO(function: Callable[[], A]) -> _IO[A]: # pylint: disable=invalid-name
    pass

IO.apply = _IO.apply
IO.insert = _IO.insert
