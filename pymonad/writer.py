from typing import Callable, Generic, TypeVar

import pymonad.monad
import pymonad.monoid

S = TypeVar('S') # pylint: disable=invalid-name
T = TypeVar('T') # pylint: disable=invalid-name

class Writer(pymonad.monad.Monad, Generic[T]):
    @classmethod
    def insert(cls, value: T) -> 'Writer[T]':
        """ See Monad.insert. """
        return cls(value, pymonad.monoid.IDENTITY)

    def bind(
            self: 'Writer[S]', kleisli_function: Callable[[S], 'Writer[T]']
    ) -> 'Writer[T]':
        pass

    def map(self: 'Writer[S]', function: Callable[[S], T]) -> 'Writer[T]':
        pass

    def __eq__(self, other):
        return self.value == other.value and self.monoid == other.monoid

    def __repr__(self):
        return f'({self.value}, {self.monoid})'
