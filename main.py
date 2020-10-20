import lists, screen, inputs
from time import sleep

error = ""
OPTIONS = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
started_first_list = False
started_second_list = False
is_first_list = True
my_first_list = lists.LinkedList()
my_second_list = lists.LinkedList()
first_list = 'Não Iniciada'
second_list = 'Não Iniciada'

while True:
    if(started_first_list):
        first_list = f'[{my_first_list}]'
    else:
        first_list = 'Não Iniciada'
    if(started_second_list):
        second_list = f'[{my_second_list}]'
    else:
        second_list = 'Não Iniciada'

    screen.exibir_Menu_Principal(first_list, second_list)
    print(error)
    op = inputs.getCatacterEmLista(OPTIONS, 'Informe a opção desejada: ', 'A posição informada é inválida')

    if(op == '0'):
        break
    
    if(op == '1'):
        if ((not started_first_list) or (not started_second_list)):
            element = inputs.getElemento("Digite o elemento que deseja inserir: ", "O elemento Inserido é inválido (Somente inteiros)")
       
            if not(started_first_list):
                my_first_list.append(element)
                started_first_list = True

            elif not(started_second_list):
                my_second_list.append(element)
                started_second_list = True

            screen.exibir_msg_sucesso()
            error = ""
            sleep(1)
        else:
            error = "Sua listas já foram criadas!"
    
    if (started_second_list and op != '1' and op != '8'):
        answer = inputs.getCatacterEmLista(['1', '2'], 'Qual lista você quer mexer? (1 ou 2)', 'A lista Informada não é válida')
        if(answer == '1'):
            is_first_list = True
        else:
            is_first_list = False

    if not(started_first_list) and not(started_second_list):
        error = "Sua lista ainda não foi criada!"
    elif(op == '2'):
        element = inputs.getElemento("Digite o elemento que deseja inserir: ", "O elemento Inserido esta apresentando erro, por favor, tente outro!")
        if(is_first_list):
            my_first_list.append(element)
        else:
            my_second_list.append(element)
        screen.exibir_msg_sucesso()
        error = ''

    elif(op == '3'):
        index = inputs.getInt("Digite a posição do elemento desejado: ", "A posição informada é inválida!")
        if(is_first_list):
            my_first_list.remove(index - 2) # Diminui dois para chegar no antecessor
        else:
            my_second_list.remove(index - 2)
    
    elif(op == '4'):
        index = inputs.getInt("Digite a posição do elemento desejado: ", "A posição informada é inválida!")
        index -= 1
        if(is_first_list):
            element = my_first_list[index]
        else:
            element = my_second_list[index]
        print(f'O elemento na posição informada é: {element}')
        sleep(3)

    elif(op == '5'):
        element = inputs.getElemento("Digite o elemento que deseja saber a posição: ", "O elemento Inserido esta apresentando erro, por favor, tente outro!")
        if(is_first_list):
            index = my_first_list.index(element)
        else:
            index = my_second_list.index(element)
        print(f'A posição do elemento informado é: {index}')
        sleep(3)

    elif(op == '6'):
        if(is_first_list):
            my_first_list.destruct()
            started_first_list = False
        else:
            my_second_list.destruct()
            started_second_list = False
            is_first_list = True
        error = ''

    elif(op == '7'):
        if(is_first_list):
            lista = my_first_list.reverse()
        else:
            lista = my_second_list.reverse()
        print(f'[{lista}]')
        error = ''
        sleep(5)
    
    elif(op == '8'):
        equal = my_first_list.equals(my_second_list)
        if(equal):
            print('As listas são Iguais')
        else:
            print('As listas são difierentes')
        sleep(5)
        

        
screen.exibir_Despedida()
sleep(3)