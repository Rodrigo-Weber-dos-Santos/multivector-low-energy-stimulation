import sys
import math
fp = open("/home/bruno/Desktop/Artigo/ArvoresCoracao/pontos_tree1.txt")
pontos = [ map(float,line.split('\t')) for line in fp ]
fl = open("/home/bruno/Desktop/Artigo/ArvoresCoracao/linhas_tree1.txt")
linhas1 = [ map(float,line.split('\t')) for line in fl ]
linhas2 = []
linhasFile = open("/home/bruno/Desktop/Artigo/ArvoresCoracao/linhas2_tree1.txt", 'w+')
for l1 in linhas1:
    ip1 = l1[0]
    fp1 = l1[1]
    achou = False
    for l2 in linhas2:
        ip2 = l2[0]
        fp2 = l2[1]
        if ip1 == fp2 and fp1 == ip2:
            #if ip1 == ip2 and fp1 == fp2:
            achou = True
    if not achou:
        linhas2.append(l1)
        #linhasFile.write(str(l1[0]))
        #linhasFile.write("\t")
        #linhasFile.write(str(l1[1]))
        #linhasFile.write("\t")
        #linhasFile.write(str(l1[2]))
        #linhasFile.write("\n")
#print(len(linhas2))
linhas3 = []
linhas3.append(linhas2[0])
heap = [linhas2[0]]
while not (len(heap) == 0):
    #print(len(linhas3))
    atual = heap.pop()
    end = atual[1]
    #print(end)
    for l2 in linhas2:
        p1 = l2[0]
        p2 = l2[1]
        if end == p1 and atual != l2:
            heap.append(l2)
            linhas3.append(l2)
        if end == p2 and atual != l2:
            aux = l2[0]
            l2[0] = l2[1]
            l2[1] = aux
            heap.append(l2)
            linhas3.append(l2)

change = True
while change:
    change = False
    linhas4 = []
    linhas4.append(linhas3[0])
    heap = [linhas3[0]]
    while not (len(heap) == 0):
        #print(len(linhas3))
        atual = heap.pop()
        end = atual[1]
        #print(end)
        son1 = -1
        son2 = -1
        for l3 in linhas3:
            p1 = l3[0]
            p2 = l3[1]
            if end == p1 and atual != l3:
                if son1 == -1: son1 = l3
                else: son2 = l3
        if son1 != -1 and son2 != -1:
            heap.append(son1)
            heap.append(son2)
            linhas4.append(son1)  
            linhas4.append(son2)
        elif son1 != -1:
            change = True
            atual[1] = son1[1]

linhas5 = []
for l4 in linhas4:
    if l4[2] > 0.1:
        linhas5.append(l4)    
            
change = True
while change:
    change = False
    linhas6 = []
    linhas6.append(linhas5[0])
    heap = [linhas5[0]]
    while not (len(heap) == 0):
        #print(len(linhas3))
        atual = heap.pop()
        end = atual[1]
        #print(end)
        son1 = -1
        son2 = -1
        for l5 in linhas5:
            p1 = l5[0]
            p2 = l5[1]
            if end == p1 and atual != l5:
                if son1 == -1: son1 = l5
                else: son2 = l5
        if son1 != -1 and son2 != -1:
            heap.append(son1)
            heap.append(son2)
            linhas6.append(son1)  
            linhas6.append(son2)
        elif son1 != -1:
            change = True
            atual[1] = son1[1]     
            
for l6 in linhas6:
    linhasFile.write(str(l6[0]))
    linhasFile.write("\t")
    linhasFile.write(str(l6[1]))
    linhasFile.write("\t")
    linhasFile.write(str(l6[2]))
    linhasFile.write("\n")
