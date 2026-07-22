
from typing import (
    Any,
    Generic,
    List,
    TypeVar,
    Union,
    Iterable,
    Self,
)  # pylint: disable=unused-import

T = TypeVar("T")  # pylint: disable=invalid-name


class Monoid[T]:

    @classmethod
    def wrap(cls, value: T) -> Self:
        pass

    def __init__(self, value: T) -> None:
        if value == None:
            raise ValueError("None Objects not allowed in Monoids")
        self.value = value

    def __add__(self, other: Self | T) -> Self:
        if not isinstance(other, self.__class__):
            if isinstance(other, Monoid):
                raise ValueError("Incompatible Monoid")
            return self.addition_operation(self.__class__(other))
        return self.addition_operation(other)

    def __eq__(
        self: Union["_MonoidIdentity", "Monoid[T]"],
        other: Union["_MonoidIdentity", "Monoid[T]"],
    ) -> bool:
        return self.value == other.value

    def addition_operation(self: Self, other: Self) -> Self:
        """Defines how monoid values are added together.

        addition_operation() method is automatically called by
        __add__() so monoid values are typically combined using the +
        operator and not addition_operation() directly.

        This method must be overridden in subclasses of Monoid.

        Args:
          other: a monoid value of the same type as self.

        Returns:
          Another monoid value of the same type as self and other.

        """
        raise NotImplementedError

    @classmethod
    def identity_element[a: "Monoid"](cls: type[a]) -> a:
        """Returns the identity value for the monoid type.

        This method must be overridden in subclasses of Monoid

        """
        raise NotImplementedError


class _MonoidIdentity[T](Monoid[T]):
    superclass = Monoid

    def __init__(self):
        found = False
        for i in type(self).__mro__:
            if (
                i != _MonoidIdentity
                and i != self.__class__
                and i != Monoid
                and i != Generic
                and i != object
            ):
                self.superclass = i
                found = True
                break
        if not found and self.__class__ != _MonoidIdentity:
            raise Exception("no superclass found")
        self.value = None

    def __add__(self: Self, other: Monoid[T] | T):
        if not isinstance(other, Monoid):
            return self.superclass(other)
        return other

    def __radd__(self, other: Self):
        if not isinstance(other, Monoid):
            return self.superclass(other)
        return other

    def __repr__(self):
        return "IDENTITY"


IDENTITY = _MonoidIdentity()


def mconcat[a: Monoid](monoid_list: Iterable[a]) -> a:
    pass
