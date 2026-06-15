import cubit
import sys
sys.path.append('/home/bruno/git/ProjetoDoutorado/CenterlinesToGeometry')
from settings import *
from arvore import Arvore
import geo
import geo2

def main():
    cubit.cmd("set warning off")
    cubit.cmd("set developer commands on")
    print "Lendo Pontos e Linhas\n"
    fp = open(folder+"pontos_tree1.txt")
    pontos = [ map(float,line.split('\t')) for line in fp ]
    fl = open(folder+"linhas2_tree1.txt")
    linhas = [ map(float,line.split('\t')) for line in fl ]
    print "Montando Árvore\n"
    arvore = Arvore(pontos, linhas)
    arvore.preProcess()
    #print "Desenhando Árvore\n"
    arvore.draw()
    arvore.smothRadius()
    arvore.makeGeometry()
    arvore.meshArvore()
    #arvore.meshNew()
    arvore.saveMesh()
    #arvore.saveMesh()
    fp.close()
    fl.close()
    
main()