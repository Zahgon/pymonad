from typing import Any, Callable, Generic, TypeVar

import pymonad.monad

S = TypeVar('S') # pylint: disable=invalid-name
T = TypeVar('T') # pylint: disable=invalid-name

class Maybe(pymonad.monad.Monad, Generic[T]):
    @classmethod
    def insert(cls, value: T) -> 'Maybe[T]':
        """ See Monad.insert """
        return cls(value, True)

    def amap(self: 'Maybe[Callable[[S], T]]', monad_value: 'Maybe[S]') -> 'Maybe[T]':
        pass

    def bind(self: 'Maybe[S]', kleisli_function: 'Callable[[S], Maybe[T]]') -> 'Maybe[T]':
        pass

    def is_just(self) -> bool:
        pass

    def is_nothing(self) -> bool:
        pass

    def map(self: 'Maybe[S]', function: Callable[[S], T]) -> 'Maybe[T]':
        pass

    def maybe(self: 'Maybe[S]', default_value: T, extraction_function: Callable[[S], T]) -> T:
        pass

    option = maybe

    def __eq__(self, other):
        """ Checks equality of Maybe objects.

        Maybe objects are equal iff:
          1. They are both Nothing, or
          2. They are both Just and
            2a. They both contain the same value.
        """
        return self.value == other.value and self.monoid == other.monoid

    def __repr__(self):
        return f'Just {self.value}' if self.monoid else 'Nothing'

def Just(value: T) -> Maybe[T]: # pylint: disable=invalid-name
    """ A Maybe object representing the presence of an optional value. """
    return Maybe(value, True)

Nothing: Maybe[Any] = Maybe(None, False) # pylint: disable=invalid-name







class Option(Maybe[T]): # MonadAlias must be the first parent class
    def __repr__(self):
        return f'Some {self.value}' if self.monoid else 'Nothing'

def Some(value: T) -> Option[T]: # pylint: disable=invalid-name
    """ An Option object representing the presence of an optional value. """
    return Option(value, True)
