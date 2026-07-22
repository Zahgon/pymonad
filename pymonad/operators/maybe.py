from typing import TypeVar

import pymonad.maybe
import pymonad.monad
import pymonad.operators.operators

T = TypeVar('T') # pylint: disable=invalid-name

class Maybe(pymonad.operators.operators.MonadOperators, pymonad.maybe.Maybe[T]): # pylint: disable=abstract-method
    pass

def Just(value: T) -> Maybe[T]: # pylint: disable=invalid-name
    """ A Maybe object representing the presence of an optional value. """
    return Maybe(value, True)

Nothing = Maybe(None, False) # pylint: disable=invalid-name





class Option(Maybe[T]): # pylint: disable=too-many-ancestors, abstract-method
    def __repr__(self):
        return f'Some {self.value}' if self.monoid else 'Nothing' # pylint: disable=no-member

def Some(value: T) -> Option[T]: # pylint: disable=invalid-name
    """ An Option object representing the presence of an optional value. """
    return Option(value, True)
