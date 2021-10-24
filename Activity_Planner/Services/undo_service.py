class UndoService:
    def __init__(self):
        self._history = []
        self._index = -1

    def undo(self):
        if self._index == -1:
            return False
        self._history[self._index].undo()
        self._index -= 1

    def redo(self):
        if self._index == len(self._history)-1:
            return False
        self._index += 1
        self._history[self._index].redo()

    def record(self, operation):
        self._history = self._history[0:self._index+1]
        self._history.append(operation)
        self._index += 1


class Operation:
    """
    Undo/Redo a program operation
    """
    def __init__(self, fun_call_undo, fun_call_redo):
        self._fun_call_undo = fun_call_undo
        self._fun_call_redo = fun_call_redo

    def undo(self):
        self._fun_call_undo()

    def redo(self):
        self._fun_call_redo()


class FunctionCall:
    """
    A function call with parameters
    """
    def __init__(self, function_reference, *function_parameters):
        self._function_ref = function_reference
        self._function_params = function_parameters

    def call(self):
        return self._function_ref(*self._function_params)

    def __call__(self):
        return self.call()
