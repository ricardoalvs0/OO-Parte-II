#coding: utf-8

__author__ = "Ricardo Alves Barbosa Filho"

class Retangulo:
    def __init__(self, largura, altura):
        self._largura = 0     # Só com métodos assessores.
        self._altura = 0      # Agora com métodos de visibilidade dos membros.
        self.altura = altura
        self.largura = largura
        #self._set_altura(altura)# (_largura)
        #self._set_largura(largura)

    '''def _get_altura(self):
        return self._altura'''
    @property
    def altura(self):
        return self._altura

    '''def _set_altura(self, num):  
           if(not(isinstance(num, int) and (num>0))):
               raise ValueError('A altura é inválida {}'.format(num))
           self._altura = num'''

    @altura.setter
    def altura(self, num):
        if (not (isinstance(num, int) and (num > 0))):
            raise ValueError('A altura é inválida {}'.format(num))
        self._altura = num


    '''def _get_largura(self):              #####################
        return self._largura'''             # OS COMENTÁRIOS SÃO#
    @property                               # OS MODELOS SEM OS #
    def largura(self):                      # DECORATORS        #
        return self._largura                #####################

    '''def _set_largura(self, num): #Se for uma função privada, ficaria (__set_largura)
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError('A largura é inválida {}'.format(num))
        self._largura = num'''
    @largura.setter
    def largura(self, num): #Se for uma função privada, ficaria (__set_largura)
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError('A largura é inválida {}'.format(num))
        self._largura = num
        #self.__var = 456
    #def _get_area(self):
     #   return self._altura * self._largura
    @property
    def area(self):
        return self._altura * self._largura

    #altura = property(fget= _get_altura, fset=_set_altura )
    #largura = property(fget= _get_largura, fset=_set_largura )
    #area = property(fget= _get_area)
a = Retangulo(3, 4)
a.largura = 10
a.altura = 15
print(a.altura)
print(a.largura)
