import ijson
import urllib
import request
import urlopen
import os

### DECLARACAO ###
#T4: HIDE, ORE, WOOD, ROCK, FIBER, PLANKS
itens_t4 = ["https://bit.ly/2LR3zag","https://bit.ly/2XibQcy","https://bit.ly/2LN0nfw","https://bit.ly/3ebMSm3","https://bit.ly/2WS9YIs","https://bit.ly/2ZoFwHs"]
itens_t5 = ["https://bit.ly/2TORiHM", "https://bit.ly/2zu8jA9", "https://bit.ly/2XyPTGc", "https://bit.ly/3ekDHQ6", "https://bit.ly/2X9I9M4","https://bit.ly/3gumaXO"]
entry = {}
continuar = 0
i = 0
### Inicio ###
while continuar != 'q': 
    #ZERANDO
    cidade =[]
    item = []
    preco = []
    ##CIDADES
    brid = []
    fort = []
    lymb = []
    mart = []
    thet = []
    tier = 0
    destinos= [brid, fort, lymb,mart,thet]
    #COMEÇANDO
    os.system('clear')
    recurso = int(input ("<0> HIDE | <1> ORE | <2> WOOD | <3> ROCK | <4> FIBER | <5> PLANKS\n\n\nEscolha o recurso:\n>"))
    if recurso > 5:
        print("Valor invalido")
        break
    ### JSON ###
    composicao = ['ORIGEM', 'ITEM', 'LUCRO', 'DESTINO']
    tier = int(input("Tier? <4> <5>\n>"))
    if tier == 4:
        url = urllib.request.urlopen(itens_t4[recurso])
    elif tier == 5:
        url = urllib.request.urlopen(itens_t5[recurso])
    elif tier >= 6 or tier < 5: 
        print("Tier invalido. Finalizando")
        break
    parser = ijson.parse(url)

    for prefix, event, value in parser:
        if prefix.endswith('city'):
            cidade.append(value)
        elif prefix.endswith('item_id'):
            item.append(value)
        elif prefix.endswith('sell_price_min'):
            preco.append(value)
        i+=1

    os.system('clear')
    ### CALCULOS ###

    #Explicação K representa a cidade de origem e L representa o destino  o primeiro laço de K diz que K tem de chegar a 0
    #Tendo seu valor padrão como o numero de cidades 0,1,2,3,4 tendo 5 porém enquanto o destino não rodar 5 vezes K não decresce
    #Dessa forma temos todos as rotas possiveis estabelecidas

    #[0]Bridgewatch, [1]Fort Sterling, [2]Lymbusg, [3]Martlock, [4]Thetford
    K = 4
    while K>=0:
        K -=1
        L = 4
        while L>=0:
            destinos[K].append(preco[L]-preco[K])
            L-=1

    ### IMPRIMINDO ###

    print('#{:-^71s}#'.format(item[0]))
    print('#{:-^71s}#'.format("PREÇOS ATUALIZADOS DE ACORDO COM AODP"))
    print ('|{0:^17}|{3:^17}|{1:^17}|{2:^17}|'.format(*composicao))
    print('|{:-^71s}|'.format(""))

    ### INVERTENDO ###

    brid = brid.reverse()
    fort = fort.reverse()
    lymb = lymb.reverse()
    mart = mart.reverse()
    thet = thet.reverse()

    ### TABELA ###
    i=4
    j=4
    while i >= 0:
        j = 4
        i -= 1
        while j >= 0:
            atual = destinos[i]
            apreco = atual[j]
            print ('|{0:^16}'.format(*cidade[i:None]),'|{0:^16}'.format(*cidade[j:None]),'|{0:^16}'.format(*item[i:None]),'|{0:^16}'.format(apreco),'|')
            j-=1
    print('#{:-^71s}#'.format(""))
    
    i = 0
    print('\n\n#{:-^53s}#'.format("Preço/Cidade"))
    while i <= 4:
        print ('|{0:^16}'.format(*cidade[i:None]),'|{0:^16}'.format(*item[i:None]),'|{0:^16}'.format(*preco[i:None]),'|')
        i+=1
    print('#{:-^53s}#'.format(""))
    print('\n\n BASEADO EM: ALBION ONLINE DATA PROJECT\n')
    continuar = input ("\n Digite \"q\" para sair, ou qualquer outra tecla para nova consulta:\n>")
#FIM WHILE