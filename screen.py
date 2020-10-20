from os import system, name

def limpar():
    if name == 'nt': # Windows
        system('cls')
    else:
        system('clear')

def exibir_Menu_Principal(first_list, second_list):
    limpar()
    print(' ======================== My Little List ====================== ')
    print('|                                                              |')
    print('|  1 - Iniciar Lista                                           |')
    print('|  2 - Inserir Elemento                                        |')
    print('|  3 - Remover Elemento                                        |')
    print('|  4 - Localizar Elemento (Posição)                            |')
    print('|  5 - Localizar Elemento (Valor)                              |')
    print('|  6 - Distruir Lista                                          |')
    print('|  7 - Exibir lista Invertida                                  |')
    print('|  8 - Comparar as Duas Listas                                 |')
    print('|  0 - Sair                                                    |')
    print('|                                                              |')
    print(' ============================================================== ')
    print()
    print(f'Primeira lista: {first_list}')
    print(f'Segunda lista: {second_list}')
    print()



def exibir_Despedida():
    limpar()
    print(' ======================== My Little List ====================== ')
    print('|                                                              |')
    print('|       O sistema será desligado em alguns instantes....       |')
    print('|                                                              |')
    print(' ============================================================== ')

def exibir_Menu_Iniciar_Lista():
    print(' ======================== My Little List ====================== ')
    print('|                                                              |')
    print('|     Para iniciar a lista primeiro precisamos de algumas      |')
    print('|                   informações, seja paciente.                |')
    print('|                                                              |')
    print(' ============================================================== ')

def exibir_Menu_Inserir_Elemento():
    print(' ======================== My Little List ====================== ')
    print('|                                                              |')
    print('|        O Elemento inserido irá substituir o antigo!          |')
    print('|                                                              |')
    print(' ============================================================== ')

def exibir_Menu_Remover_Elemento():
    limpar()
    print(' ======================== My Little List ====================== ')
    print('|                                                              |')
    print('|                Removendo Elemento da Lista....               |')
    print('|                                                              |')
    print(' ============================================================== ')

def exibir_Menu_Localizar_Elemento():
    limpar()
    print(' ======================== My Little List ====================== ')
    print('|                                                              |')
    print('|              Elemento sendo procurado na Lista....           |')
    print('|                                                              |')
    print(' ============================================================== ')

def exibir_Menu_Apagar_Lista():
    limpar()
    print(' ======================== My Little List ====================== ')
    print('|                                                              |')
    print('|                       Lista sendo limpa....                  |')
    print('|                                                              |')
    print(' ============================================================== ')

def exibir_msg_sucesso():
    limpar()
    print(' ======================== My Little List ====================== ')
    print('|                                                              |')
    print('|                Alteração realizada com sucesso!              |')
    print('|                                                              |')
    print(' ============================================================== ')

def exibir():
    pass