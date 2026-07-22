import pymonad.monad

class MonadOperators(pymonad.monad.Monad): # pylint: disable=abstract-method
    def __and__(self, monad_value):
        return self.amap(monad_value)

    def __rmul__(self, function):
        return self.map(function)

    def __rshift__(self, kleisli_function):
        return self.bind(kleisli_function)
