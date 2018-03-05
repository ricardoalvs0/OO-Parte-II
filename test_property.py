#coding: utf-8

__author__ = "Ricardo Alves Barbosa Filho"

class A:
    def __init__(self):
        self._var = 0
    @property
    def var(self):
        print('O valor está sendo lido.')
        return self._var
    @var.setter
    def var(self, x):
        print('O valor está sendo escrito.')
        self._var = x

a = A()
a.var = 10
t = a.var
  #  var = property(fget=_get_var, fset=_set_var)
'''
#       Classe sem decorators
class A:
    def __init__(self):
        self._x = 0

    def get_x(self):
        return self._x
    x = property (fget=get_x)

#       Classe com decorators
class A1:
    def __init__(self):
        self._x = 0
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, val):
        self._x = val'''