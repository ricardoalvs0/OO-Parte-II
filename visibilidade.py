'''                        VISIBILIDADE DOS MEMBROS
---> Embora o Python não possua um modo de inviabilizar o acesso aos membros de uma
     classe, algumas técnicas e convenções podem ser utilizadas.

     Convenção 1: Membros que são exclusivamente internos ao objeto devem ter seus nomes começados
     por um underline:
                publico = 0
                _restrito = 0

     Convenção 2(colisão de nomes): Para evitar a colisão de nomes entre a superclasse e a subclasse
     o membro deve ser precedido por dois underlines:
                __colisao = 0

     Convenção 3(métodos mágicos): São precedidos e finalizados com dois underlines e são exclusivos da linguagem
     (dunder) = dois underlines
'''
