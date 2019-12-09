from abc import abstractmethod


def puzzle_input(path):
    with open(path, 'r') as f:
        prompt = f.read()

    return prompt.split()


class Intcode:

    MAX_PARAMS = 5

    def __init__(self, codes):
        self.codes = codes
        self.i = 0
        self.base = 0
        self.input = 0

    @abstractmethod
    def _input(self):
        pass

    @abstractmethod
    def _output(self, out):
        pass

    def _param_loc(self, inc, modes):
        mode = modes[self.MAX_PARAMS - 2 - inc]
        return self.i + inc if mode == 1 else self.codes[self.i + inc] + self.base if mode == 2 else self.codes[self.i + inc]

    def _param(self, inc, modes):
        return self.codes[self._param_loc(inc, modes)]

    def _execute(self, op, modes):
        if op == 1:
            self.codes[self._param_loc(3, modes)] = self._param(1, modes) + self._param(2, modes)
            self.i += 4
        elif op == 2:
            self.codes[self._param_loc(3, modes)] = self._param(1, modes) * self._param(2, modes)
            self.i += 4
        elif op == 3:
            self.codes[self._param_loc(1, modes)] = self._input()
            self.i += 2
        elif op == 4:
            self._output(self._param(1, modes))
            self.i += 2
        elif op == 5:
            if self._param(1, modes) != 0:
                self.i = self._param(2, modes)
            else:
                self.i += 3
        elif op == 6:
            if self._param(1, modes) == 0:
                self.i = self._param(2, modes)
            else:
                self.i += 3
        elif op == 7:
            self.codes[self._param_loc(3, modes)] = 1 if self._param(1, modes) < self._param(2, modes) else 0
            self.i += 4
        elif op == 8:
            self.codes[self._param_loc(3, modes)] = 1 if self._param(1, modes) == self._param(2, modes) else 0
            self.i += 4
        elif op == 9:
            self.base += self._param(1, modes)
            self.i += 2
        else:
            assert op == 99, op
            raise EOFError

    def run(self, i=None):

        if i is not None:
            self.i = i

        while True:
            k = str(self.codes[self.i])

            while len(k) < self.MAX_PARAMS:
                k = "0" + k

            modes = int(k[0]), int(k[1]), int(k[2])
            op = int(k[3:])

            while True:
                try:
                    self._execute(op, modes)
                    break
                except IndexError:
                    self.codes += [0]
                except EOFError:
                    return
