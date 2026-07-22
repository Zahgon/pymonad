from typing import Any, Callable, Generic, List, TypeVar, Union # pylint: disable=unused-import

import pymonad.monad
import pymonad.monoid

S = TypeVar('S') # pylint: disable=invalid-name
T = TypeVar('T') # pylint: disable=invalid-name

class _List(pymonad.monad.Monad, pymonad.monoid.Monoid, Generic[T]):
    @classmethod
    def insert(cls, value: T) -> '_List[T]':
        return cls([value], None)

    @staticmethod
    def identity_element() -> '_List[Any]':
        pass

    def amap(self: '_List[Callable[[S], T]]', monad_value: '_List[S]') -> '_List[T]':
        pass

    def bind(self: '_List[S]', kleisli_function: Callable[[S], '_List[T]']) -> '_List[T]':
        pass

    def join(self: '_List[_List[T]]') -> '_List[T]':
        pass

    def map(self: '_List[S]', function: Callable[[S], T]) -> '_List[T]':
        pass

    def then(
            self: '_List[S]', function: Union[Callable[[S], T], Callable[[S], '_List[T]']]
    ) -> '_List[T]':
        pass

    def addition_operation(self, other):
        pass

    def __eq__(self, other):
        return self.value == other.value

    def __getitem__(self, index):
        result = self.value.__getitem__(index)
        try:
            if len(result) > 0:
                result_list = self.__class__(result, None)
            return result_list
        except TypeError:
            return result

    def __iter__(self):
        return iter(self.value)

    def __len__(self):
        return len(self.value)

    def __repr__(self):
        return str(self.value)

def ListMonad(*elements: List[T]) -> _List[T]: # pylint: disable=invalid-name
    """ Creates an instance of the List monad.

    Args:
      *elements: any number of elements to be inserted into the list

    Returns:
      An instance of the List monad.
    """

    return _List(list(elements), None)

ListMonad.insert = _List.insert
ListMonad.apply = _List.apply
ListMonad.identity_element = _List.identity_element
