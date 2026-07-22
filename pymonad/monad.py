
from typing import Any # pylint: disable=unused-import
from typing import Callable, Generic, TypeVar, Union

S = TypeVar('S') # pylint: disable=invalid-name
T = TypeVar('T') # pylint: disable=invalid-name

class Monad(Generic[T]):
    def __init__(self, value, monoid):
        """ Initializes the internal values of the monad instance.

        All monads can be expressed as a tuple, (a, m). Representing
        all monads internally in this canonical form allows for some
        interesting effects such as easily aliasing existing monads
        instances and, if desired, adding operators. Occasionally it
        also makes implementation of the monad methods itself easier.

        Args:
          value: if we think of monads as storing some data of
            interest plus some 'meta data', then 'value' is the data of
            interest. Exactly what 'value' is/means will depend on the
            specific context of the monad in question.
          monoid: this is the 'meta data' part. While implementers may
            use an instance of the Monoid class here it is not
            required. However, the value passed in here should be a type
            that can be treated as a monoid, such as integers; strings;
            lists; etc., in order to ensure that the monad laws are
            obeyed. This is not enforced but it will result in an
            incorrect implementation.
        """
        self.value = value
        self.monoid = monoid

    @classmethod
    def apply(cls, function):
        pass

    @classmethod
    def insert(cls, value: T) -> 'Monad[T]':
        """ Returns an instance of the Functor with 'value' in a minimum context.  """
        raise NotImplementedError

    def amap(self: 'Monad[Callable[[S], T]]', monad_value: 'Monad[S]') -> 'Monad[T]':
        pass

    def bind(self: 'Monad[S]', kleisli_function: Callable[[S], 'Monad[T]']) -> 'Monad[T]':
        """ Applies 'function' to the result of a previous monadic calculation. """
        raise NotImplementedError

    def join(self: 'Monad[Monad[T]]') -> 'Monad[T]':
        pass

    def map(self: 'Monad[S]', function: Callable[[S], T]) -> 'Monad[T]':
        """ Applies 'function' to the contents of the functor and returns a new functor value. """
        raise NotImplementedError("'fmap' not defined.")

    def then(
            self: 'Monad[S]', function: Union[Callable[[S], T], Callable[[S], 'Monad[T]']]
    ) -> 'Monad[T]':
        pass
