import ply.lex as lex
import re
import codecs
import os
import sys


# resultado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
    'main', 'if', 'then', 'else', 'end', 'do', 'while', 'repeat', 'until', 'cin', 'cout', 'real', 'int', 'boolean'
)
tokens = reservada + (

#Simbolos especiales['+', '-', '*', '/', '%', '<', '<=', '>', '>=', '==', '!=', ':=', '(', ')', '{', '}', '//', '/*', '++', '--']
#otros escenciales['=',',',';','>>','<<','"',':']

    'IDENTIFICADOR',
    'ENTERO',
    'FLOTANTE',

    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'MODULO',
    'MINUSMINUS',
    'PLUSPLUS',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    'PARIZQ',
    'PARDER',
    'LLAIZQ',
    'LLADER',

    'ASIGNAR',
    'ASIGNARO',
    'DOSPUNTOS',
    'PUNTOCOMA',
    'COMA',
    'COMDOB',
    'MAYORDER', #>>
    'MAYORIZQ', #<<
)

# Reglas de Expresiones Regualres para token de Contexto simple

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_ASIGNAR = r'='
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = ';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_COMDOB = r'\"'
t_DOSPUNTOS = r'\:'


def t_main(t):
    r'main'
    return t

def t_if(t):
    r'if'
    return t

def t_then(t):
    r'then'
    return t

def t_else(t):
    r'else'
    return t

def t_end(t):
    r'end'
    return t

def t_do(t):
    r'do'
    return t

def t_while(t):
    r'while'
    return t

def t_repeat(t):
    r'repeat'
    return t

def t_until(t):
    r'until'
    return t

def t_cin(t):
    r'cin'
    return t

def t_cout(t):
   r'cout'
   return t

def t_real(t):
   r'real'
   return t

def t_int(t):
    r'int'
    return t

def t_boolean(t):
    r'boolean'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_CADENA(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

#def t_FLOTANTE(t):
    #r'\d+\.\d+'
    #t.value = float(t.value)
 #   return t

def t_ASIGNARO(t):
    r'\:='
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MINUSMINUS(t):
    r'\-\-'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_MAYORDER(t):
    r'<<'
    return t

def t_MAYORIZQ(t):
    r'>>'
    return t

def t_DISTINTO(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")
    #return t

def t_comments_ONELine(t):
     r'\/\/(.)*\n'
     t.lexer.lineno += 1
     print("Comentario de una linea")
     #return t

t_ignore =' \t'

def t_error( t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)


def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)
        print(base)
        print(dirs)
        print(files)
    for file in files:
        print(str(cont)+". "+file)
        cont = cont+1

    while respuesta == False:
        numArchivo = input('\nNumeros del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break

    print("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

    return files[int(numArchivo)-1]

directorio = 'C:/Users/vuudu/Documents/Compilador/Compilador'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()




def prueba(cadena):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(cadena)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

 # instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
        #data = input("ingrese: ")
        prueba(cadena)
        print(resultado_lexema)
        archivo = open("salida.txt", "w")
        archivo.write(str(resultado_lexema))
        archivo.close() 
