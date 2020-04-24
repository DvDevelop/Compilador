#!/usr/bin/python

import sys
import time
import ply.lex as lex
import re
import codecs
import os

"""
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))


print(sys.argv)
if(len(sys.argv)>1):
    print("pass")
    print(sys.argv[1])
else:
    print("no pasas")
"""


#print('empieza...')

###################

# LÉXICO ***************************************************************************************************************
def main():
    reservadas=["main","if","then","else","end","do","while","repeat","until","real","cin","cout","int","boolean","float"]
    letras=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m","Q","W","E","R",
            "T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Ñ","Z","X","C","V","B","N","M"]
    digito=["0","1","2","3","4","5","6","7","8","9"]
    signo=["+","-"]
    operador=["!","<",">","="]
    estado=0
    especial=["(",")","{","}",";","%",","]
    comentario=""
    identificador=""
    error=0
    bandError=0
    numeroLinea=0
    archivo=open(sys.argv[1],"r")
    linesfilelist = archivo.readlines()
    token=open("token.txt","w")
    errores=open("errores.txt","w")
    for cadena in linesfilelist:
        numeroLinea=numeroLinea+1
        tam=len(cadena)
        a=0
        while(a<tam):
            caracter=cadena[a]
            if(estado==0):
                if(caracter=="/"):
                    estado=1
                    a=a+1
                    aux=caracter
                    error = 1
                if(caracter==":"):
                    estado=2
                    a = a + 1
                    aux = caracter
                    error = 1
                if(caracter in letras):
                    estado=3
                    a = a + 1
                    aux = caracter
                    error = 1
                if(caracter in digito):
                    estado=4
                    a = a + 1
                    aux = caracter
                    error = 1
                if(caracter in signo):
                    estado=5
                    a = a + 1
                    aux = caracter
                    error = 1
                if(caracter in operador):
                    estado=6
                    a = a + 1
                    aux = caracter
                    error = 1
                if(caracter in especial):
                    a = a + 1
                    error=1
                    estado=0
                    if(caracter == ','):
                        #print(caracter, "-> especial :",numeroLinea)
                        token.write(caracter+ " -> coma "+"\n")  #+numeroLinea.__str__()
                    if(caracter == ';'):
                        #print(caracter, "-> especial :",numeroLinea)
                        token.write(caracter+ " -> punto y coma "+"\n")  #+numeroLinea.__str__()
                    if(caracter != ',' and caracter != ';'):
                        #print(caracter, "-> especial :",numeroLinea)
                        token.write(caracter+ " -> especial "+"\n")  #+numeroLinea.__str__() 
                if(caracter==" " or caracter=="\n" or caracter=="\t"):
                    error=1
                    a=a+1
                    estado=0
                if (caracter == "*"):
                    error = 1
                    a = a + 1
                    #print("* -> operador:",numeroLinea)
                    token.write("* -> operador "+"\n")  #+numeroLinea.__str__()
                    estado = 0
                if(error==0):
                    #print(caracter," -> error")
                    errores.write(caracter+" -> error\n")
                    bandError=1
                    a=a+1
                    estado=0
                error=0
                continue
            if(estado==1):
                if(caracter=="/"):
                    estado=8
                    a=a+1
                    continue
                if(caracter=="*"):
                    estado=9
                    a=a+1
                    continue
                #print(aux," -> operador:",numeroLinea)
                token.write(aux+" -> operador "+"\n")  #+numeroLinea.__str__()
                estado=0
                continue
            if(estado==2):
                if(caracter=="="):
                    a=a+1
                    aux=aux+caracter
                    #print(aux,"-> asignación:",numeroLinea)
                    token.write(aux+" -> asignacion "+"\n")  #+numeroLinea.__str__()
                    estado=0
                    continue
                bandError = 1
                #print(aux," -> error")
                errores.write(aux + " -> error\n")
                estado=0
                continue
            if(estado==3):
                if(caracter in letras or caracter in digito):
                    aux=aux+caracter
                    a=a+1
                    continue
                if(aux in reservadas):
                    #print(aux,"-> palabra reservada:",numeroLinea)
                    token.write(aux + " -> PalabraReservada "+"\n") #+numeroLinea.__str__()
                    estado=0
                    continue
                #print(aux,"-> identificador",numeroLinea)
                token.write(aux + " -> identificador "+"\n")  #+numeroLinea.__str__()
                estado=0
                continue
            if(estado==4):
                if(caracter in digito):
                    aux=aux+caracter
                    a=a+1
                    continue
                if(caracter=="."):
                    estado=11
                    aux=aux+caracter
                    a=a+1
                    continue
                #print(aux,"-> entero:",numeroLinea)
                token.write(aux + " -> entero "+"\n")  #+numeroLinea.__str__()
                estado=0
                continue
            if(estado==5):
                if(caracter==aux):
                    aux=aux+caracter
                    #print(aux,"-> operador:",numeroLinea)
                    token.write(aux + " -> operador "+"\n") #+numeroLinea.__str__()
                    a=a+1
                    estado=0
                    continue
               # if(caracter in digito):
                #    aux=aux+caracter
                 #   estado=4
                  #  a=a+1
                   # continue
                #print(aux,"-> operador:",numeroLinea)
                token.write(aux + " -> operador "+"\n") #+numeroLinea.__str__()
                estado=0
                continue
            if(estado==6):
                if(caracter=="="):
                    a=a+1
                    aux=aux+caracter
                    #print(aux,"-> operador:",numeroLinea)
                    token.write(aux + " -> operador "+"\n") #+numeroLinea.__str__()
                    estado=0
                    continue
                if(aux=="=" or aux=="!"):
                    bandError = 1
                    #print(aux, "-> error")
                    errores.write(aux + " -> error\n")
                    estado=0
                    continue
                #print(aux,"-> operador:",numeroLinea)
                token.write(aux + " -> operador "+"\n") #+numeroLinea.__str__()
                estado=0
                continue
            if(estado==8):
                a=a+1
                if(a==tam):
                    estado=0
                   # print(comentario,"= comentario 1 linea")
            #        token.write(comentario + " = comentario 1 linea\n")
                    comentario=""
                else:
                    comentario = comentario + caracter
                continue
            if(estado==9):
                a=a+1
                if(caracter=="*"):
                    estado=10
                    continue
                comentario=comentario+caracter
                continue
            if(estado==10):
                a=a+1
                if(caracter=="*"):
                    band2=1
                    comentario=comentario+"*"
                    continue
                if(caracter=="/"):
                    band2=1
                    estado = 0
                #    print(comentario, "= comentario multi linea")
               #     token.write(comentario + " = comentario multi linea\n")
                    comentario = ""
                    continue
                comentario=comentario+"*"+caracter
                estado=9
                continue
            if(estado==11):
                if(caracter in digito):
                    aux=aux+caracter
                    estado=12
                    a=a+1
                    continue
                bandError = 1
                #print(aux, " -> error")
                errores.write(aux + " -> error\n") ######################################################################
                estado=0
                continue
            if(estado==12):
                if (caracter in digito):
                    aux = aux + caracter
                    a=a+1
                    continue
                #print(aux, "-> flotante:",numeroLinea)
                token.write(aux + " -> flotante "+"\n") #+numeroLinea.__str__()
                estado=0
                continue
    if(estado==3):
        if (aux in reservadas):
            #print(aux, "-> palabra Reservada:",numeroLinea)
            token.write(aux + " -> PalabraReservada "+"\n") #+numeroLinea.__str__()
        else:
            #print(aux, "-> identificador:",numeroLinea)
            token.write(aux + " -> identificador "+"\n") #+numeroLinea.__str__()
    if(estado==4):
        #print(aux, "-> entero:",numeroLinea)
        token.write(aux + " -> entero "+"\n") #+numeroLinea.__str__()
    if (estado == 12):
            #print(aux, "-> flotante")
            token.write(aux + " -> flotante "+"\n") #+numeroLinea.__str__()


    archivo.close()
    token.close()
    errores.close()


print(sys.argv[1])
main()

time.sleep(5)
