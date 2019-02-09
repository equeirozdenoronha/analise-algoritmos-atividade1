import csv
import time
def escreve(path):
    pathF = path+'.csv'
    with open(pathF) as csvFile:
        vouF = False
        linha = []
        num = csv.reader(csvFile, delimiter=';')
        for i in num:
            linha.append(i)
        valor = linha[0]
        linha.pop(0)
        linha.pop(0)
        pt = len(linha)
        cont = -1
        for i in linha:
            if i == valor:
                vouF = True
                pt = cont
            else:
                vouF = False
                pt = -1
            cont = cont+1
        fim = time.time()
        if vouF == True:
            vouF = 'True'
        else:
            vouF = 'False'
        pathResposta = 'resposta-'+ path+'.txt'
        print
        with open(pathResposta, 'w') as arq:
            pt = str(pt)
            fim = str(fim)
            arq.write(str("Existe:"+vouF+"\n"))
            arq.write(str("Posição:"+pt+'\n'))
            arq.write(str("Milisegundos:"+fim+'\n'))
    

DSa = 'dataset-1-a'
DSb = 'dataset-1-b'
DSc = 'dataset-1-c'

escreve(DSa)
escreve(DSb)
escreve(DSc)    
        
