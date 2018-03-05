'''                              PROPRIEDADES
---> property()
     property(fget, fset, fdel, doc)

---> Substitui o uso dos métodos get e set, restringindo a somente uma variável.


     DECORATORS: Funções que permitem o acesso indireto a outras funções.
     Serve pra ajudar na estética do código, facilitando a leitura do código.

     Exemplo:

     class A:
         def __init__(self):
             self._x = 0
     @property ---> confere o getter da classe
         def x(self):
             return self._x
     @x.setter ---> 'x' se refere à propriedade que está sendo definida acima.
         def x(self, val): 'setter' é a ação a ser desempenhada
             self._x = val


'''
