import asyncio
from typing import Callable, Generic, TypeVar, Union, Awaitable

import pymonad.monad
import pymonad.tools

S = TypeVar('S') # pylint: disable=invalid-name
T = TypeVar('T') # pylint: disable=invalid-name

ResolveFunction = Callable[[S], T]
RejectFunction = Callable[[Exception], T]
PromiseFunction = Callable[[ResolveFunction, RejectFunction], T]

def _reject(error):
    pass

class _Promise(pymonad.monad.Monad, Generic[T]):
    def __init__(self, value, monoid):
        super().__init__(value, monoid)
        self._resolve = pymonad.tools.identity

    @classmethod
    def insert(cls, value: T) -> '_Promise[T]':
        """ See Monad.insert. """
        return Promise(lambda resolve, reject: resolve(value))

    def amap(self: '_Promise[Callable[[S], T]]', monad_value: '_Promise[S]') -> '_Promise[T]':
        pass

    def bind(self: '_Promise[S]', kleisli_function: Callable[[S], '_Promise[T]']) -> '_Promise[T]':
        pass

    def catch(self: '_Promise[T]', error_handler: Callable[[Exception], T]) -> '_Promise[T]':
        pass

    def map(self: '_Promise[S]', function: Callable[[S], T]) -> '_Promise[T]':
        pass

    def then(
            self: '_Promise[S]', function: Union[Callable[[S], T], Callable[[S], '_Promise[T]']]
    ) -> '_Promise[T]':
        pass

    def __await__(self):
        return self.value(self._resolve, _reject).__await__()

def Promise(function: PromiseFunction) -> _Promise[T]: # pylint: disable=invalid-name
    """ Constructs a Promise object for ordering concurrent computations.

    Example:
      Promise(lambda resolve, reject: resolve('any value'))

      def some_computation(resolve, reject):
          if True:
              return resolve(10)
          else:
              reject(TypeError('Fake error.')) # doesn't need to be returned
      Promise(some_computation)

    Arguments:
      function: a function taking two callback typically called
        'resolve' and 'reject'. When the computation is successful the
        value should be returned by calling resolve with the result. If
        there is an error, call 'reject' with an instance of the
        Exception class.

    Returns:
      A new Promise object.
    """
    @pymonad.tools.curry(3)
    async def _awaitable(function, resolve, reject):
        return function(resolve, reject)
    return _Promise(_awaitable(function), None) # pylint: disable=no-value-for-parameter


def async_func(func: Callable) -> Callable:
    """Transform simple function in async function using promises.

    async_func is supposed to be used as a decorator for providing
    seamless integration with asynchronous operations, by deferring
    arguments and keyword arguments input to be scheduled asynchronously
    into the event-loop. It also transform the output into a promise,
    allowing for abstract computation.

    Example:
      @async_func
      def add(x, y):
          return x+y

      x = (Promise.insert(1)
                      .then(long_id))
      y = (Promise
              .insert(2)
              .then(long_id)
              .then(div(0))            # Raises an error...
              .catch(lambda error: 2)) # ...which is dealth with here.

      z = add(x, y)

      # z is now a Promise object that can be further used into other
      # operations, abstracting chain of computations

      print( await z.map(long_id).catch(lambda error: 'Recovering...') )

    Args:
      func: a regular function with variable arguments args and keyword
            arguments kwargs

     Returns:
      An asynchronous counterpart of the provided function, that
      accepts both promise and/or regular values and  returns promises,
      for asynchronous usage

    """

    async def getArgs(args):
        return await asyncio.gather(
            *[arg if isinstance(arg, Awaitable) else Promise.insert(arg) for arg in args]
        )

    async def getKwargs(kwargs):
        kwargsTasks = [arg.map(lambda x: (ith, x)) if isinstance(arg, Awaitable) else Promise.insert((ith, arg))
                       for ith, arg in kwargs.items()]
        return dict(await asyncio.gather(*kwargsTasks))

    async def async_wrap(*args, **kwargs):
        (_args, _kwargs) = await asyncio.gather(getArgs(args), getKwargs(kwargs))

        return func(*_args, **_kwargs)

    def wrapper(*args, **kwargs):
        pass

    return wrapper


Promise.apply = _Promise.apply
Promise.insert = _Promise.insert
