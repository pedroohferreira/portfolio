def AbreConta(listaContas):
  while True:
    try:
      existe = False
      mesa = int(input("\nQual o número da mesa: "))
      for i in listaContas: # Verificando se a mesa já existe
        if i['numeroMesa'] == mesa:
          existe = True

      if existe == True:
        print("\nEssa mesa já está ocupada!")
      else:
        garcom = input("Qual o nome do garçom: ")

        listaContas.append({'numeroMesa': mesa, 'itens': [], 'garçom': garcom})
        print("\nConta aberta!")
        return listaContas
    except ValueError:
      print("\nAo informar a mesa, digite apenas números.")

def AdicionarItens(listaContas):
  a = open("dados_restaurante.txt", 'a')
  while True:
    try:
      print("Mesas com contas abertas ", end=" |")
      for i in listaContas:
        print(f" {i['numeroMesa']} ",end="|")

      mesa = int(input("\nInforme o número da mesa: "))

      posicao = 0
      encontrei = False
      while posicao < len(listaContas) and encontrei == False:

        if listaContas[posicao]['numeroMesa'] == mesa: # Encontrando a mesa informada
          encontrei = True
          while True:
            item = str(input("\ninforme o pedido ou 'n' para sair: "))
            if item != 'n':
              qnt = int(input("Informe a quantidade: "))
              valorUnitario = float(input("Informe o valor unitário: "))

              listaContas[posicao]['itens'].append({'item': item, 'quantidade': qnt, 'valor': valorUnitario}) # Adicionando itens na mesa
              a.write(f"{item};{qnt};{valorUnitario};{mesa};{listaContas[posicao]['garçom']}")
              print("\nPedido confirmado!")
            else:
              break
          a.close()
          return listaContas
        posicao += 1
      if encontrei == False:
        print("\nNúmero de mesa não encontrado")
    except ValueError:
      print("\nAo informar a mesa, digite apenas números.")

def FecharConta(listaContas, historico):
  while True:
    try:
      print("Mesas com contas abertas ", end=" |")
      for i in listaContas:
        print(f" {i['numeroMesa']} ",end="|")
      mesa = int(input("\nInforme o número da mesa ou '0' para sair: "))
      if mesa == 0:
        return None
      encontrei = False
      posicao = 0
      while posicao < len(listaContas) and encontrei == False:
        if listaContas[posicao]['numeroMesa'] == mesa:
          encontrei = True
          total = 0
          for pedido in listaContas[posicao]['itens']:         # somando todos os pedidos que foram realizados em uma mesa
            total += pedido['quantidade'] * pedido['valor']

          # Calculando os 10%, adicionando pedido no histórico e retornando o valor do pedido e o nome do garçom
          total += total*0.1

          if total > 0:
            historico.append(listaContas[posicao])
            garcom = listaContas[posicao]['garçom']
            del listaContas[posicao]
            print("\nConta fechada!")
            return {'valorPedido': total, 'garçom': garcom}
          else:
            del listaContas[posicao]
            print("\nConta fechada!")
            return None
        posicao += 1

      if encontrei == False:
        print("\nNúmero de mesa não encontrado")
    except ValueError:
      print("\nAo informar a mesa, digite apenas números.")

def Gorjeta(contasEncerradas):
  gorjeta = 0
  garcom = str(input("Informe o nome do garçom: "))

  encontrei = False
  for i in contasEncerradas: # Percorrendo as contas fechadas para encontrar o garçom e posteriomente calcular a gorjeta dele
    if i['garçom'] == garcom:
      encontrei = True
      gorjeta += i['valorPedido'] - (i['valorPedido']/1.1)

  if encontrei == False:
    print("\nGarçom não encontrado")
  else:
    return print(f"{garcom} vai receber R${gorjeta: .2f}")

def FechamentoDia(contasEncerradas):
  faturamento = 0
  # Somando o valor de todas as contas fechadas para calcular o faturamento
  for i in contasEncerradas:
    faturamento += i['valorPedido']
  return print(f"\nO valor faturado hoje foi de R${faturamento: .2f}")

def VerHistorico(historico):
  for i in historico:
    print(f"\n   Mesa: {i['numeroMesa']}     garçom: {i['garçom']}\n")
    for x in i['itens']:
      print(f"{x['item']} - {x['quantidade']} x {x['valor']} = {x['quantidade']*x['valor']: .2f}")
    print("\n")


listaContas = [{'numeroMesa': 1,
  'itens': [{'item': 'coca-cola 2L', 'quantidade': 12, 'valor': 10.0},
   {'item': 'porção de batata', 'quantidade': 2, 'valor': 30.0}],
  'garçom': 'pedro'}]
contasEncerradas = []
historico = []

print("----------  BEM VINDO  ----------")
while True:

  print("\nO que deseja fazer?")
  print("1 - abrir conta\n2 - adicionar itens\n3 - fechar conta\n4 - calcular gorjeta\n5 - calcular faturamento\n6 - ver histórico de vendas\n'N' - para encerrar o expediente")
  opc = str(input("Qual sua opção: "))

  if opc == '1':
    AbreConta(listaContas)

  elif opc == '2':
    AdicionarItens(listaContas)

  elif opc == '3':
    retorno = FecharConta(listaContas, historico)
    if retorno != None:
      contasEncerradas.append(retorno)
  elif opc == '4':
    Gorjeta(contasEncerradas)

  elif opc == '5':
    FechamentoDia(contasEncerradas)

  elif opc == '6':
    VerHistorico(historico)

  elif opc == 'n' or opc == 'N':
    if str(input("\nDeseja mesmo encerrar o expediente?\npressione 's' para confirmar ou qualquer tecla para voltar ao menu: ")) == 's':
      if len(listaContas) == 0:
        break
      else:
        print("\nAinda existem contas abertas. Encerre as contas para encerrar o expediente.")

  else:
    print("\nDigite uma opção válida")
