import ijson
import urllib
import request
import urlopen
import os

### DECLARACAO ###
#T4: HIDE, ORE, WOOD, ROCK, FIBER, PLANKS
base = 'https://www.albion-online-data.com/api/v2/stats/prices/'
_tier = ['ERRO','ERRO','T2','T3','T4','T5','T6','T6','T7','T8']
recursos =  ['_HIDE?', '_ORE?', '_WOOD?', '_ROCK?', '_FIBER?', '_PLANKS?', '_CLOTH?', '_LEATHER?', '_METALBAR?']
localizacao = 'locations=Bridgewatch,Fort%20Sterling,Lymhurst,Martlock,Thetford&qualities=1'
link = ''

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
    recurso = int(input ("<0> HIDE | PELEGO \n<1> ORE | MINERIO\n<2> WOOD | MADEIRA\n<3> ROCK | PEDRA\n<4> FIBER | FIBRA\n<5> PLANKS | TABUAS\n<6> CLOTH | TECIDO\n<7> LEATHER | COURO\n<8> METALBAR | BARRA DE METAL\n<9> STONEBLOCK | BLOCO DE PEDRA\n\nEscolha o recurso:\n>"))
    if recurso > 9:
        print("Valor invalido")
        break
    ### JSON ###
    composicao = ['ORIGEM', 'ITEM', 'LUCRO', 'DESTINO']
    tier = int(input("Tier? <2> <3> <4> <5> <6> <7> <8>\n>"))
    if tier > 9 or tier < 2 or tier == 0 or tier == 1: 
        print("Tier invalido. Finalizando")
        break
    link = base + str(_tier[tier]) + str(recursos[recurso]) + localizacao
    url = urllib.request.urlopen(link)
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