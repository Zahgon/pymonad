from typing import Any, Callable, Generic, TypeVar

import pymonad.monad

M = TypeVar('M') # pylint: disable=invalid-name
S = TypeVar('S') # pylint: disable=invalid-name
T = TypeVar('T') # pylint: disable=invalid-name

class Either(pymonad.monad.Monad, Generic[M, T]):
    @classmethod
    def insert(cls, value: T) -> 'Either[Any, T]':
        """ See Monad.insert """
        return cls(value, (None, True))

    def amap(self: 'Either[M, Callable[[S], T]]', monad_value: 'Either[M, S]') -> 'Either[M, T]':
        pass

    def bind(
            self: 'Either[M, S]', kleisli_function: Callable[[S], 'Either[M, T]']
    ) -> 'Either[M, T]':
        pass

    def either(
            self: 'Either[M, S]', left_function: Callable[[M], T], right_function: Callable[[S], T]
    ) -> T:
        pass

    def is_left(self) -> bool:
        pass

    def is_right(self) -> bool:
        pass

    def map(self: 'Either[M, S]', function: Callable[[S], T]) -> 'Either[M, T]':
        pass

    def __eq__(self, other):
        """ Checks equality of Maybe objects.

        Maybe objects are equal iff:
          1. They are both Nothing, or
          2. They are both Just and
            2a. They both contain the same value.
        """
        return self.value == other.value and self.monoid == other.monoid

    def __repr__(self):
        return f'Right {self.value}' if self.is_right() else f'Left {self.monoid[0]}'

def Left(value: M) -> Either[M, Any]: # pylint: disable=invalid-name
    """ Creates a value of the first possible type in the Either monad. """
    return Either(None, (value, False))

def Right(value: T) -> Either[Any, T]: # pylint: disable=invalid-name
    """ Creates a value of the second possible type in the Either monad. """
    return Either(value, (None, True))






class _Error(Either[M, T]):
    def __repr__(self):
        return f'Result: {self.value}' if self.is_right() else f'Error: {self.monoid[0]}'

def Error(value: M) -> _Error[M, Any]: # pylint: disable=invalid-name
    """ Creates an error value as the result of a calculation. """
    return _Error(None, (value, False))

def Result(value: T) -> _Error[Any, T]: # pylint: disable=invalid-name
    """ Creates a value representing the successful result of a calculation. """
    return _Error(value, (None, True))

Error.apply = _Error.apply
Error.insert = _Error.insert
