class Foo(object):
    @property
    def bar(self):
        return self._bar

    @bar.setter
    def bar(self, new_bar):
        self._bar = new_bar


f = Foo()
f.bar = 100
print(f.bar)
