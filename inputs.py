def getInt(msg_pedido, msg_erro):
  while True:
    resposta = input(msg_pedido)
    try:
      int(resposta)
      break
    except:
      print(msg_erro)
  return int(resposta)

def getCatacterEmLista(vetor, msg_pedido, msg_erro):
  while True:
    resposta = input(msg_pedido)
    if(resposta in vetor):
      break
    else:
      print(msg_erro)
  return resposta

def getElemento(msg_pedido, msg_erro):
  resposta = ""
  while True:
    try:
      resposta = input(msg_pedido)
      break
    except:
      print(msg_erro)
  return resposta