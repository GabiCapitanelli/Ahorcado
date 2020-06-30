import random
import time
from os import system
from project.models import db, Universo
from flask import session
from sqlalchemy.sql.expression import func

class Ahorcado():

    def __init__(self):
        self.palabras = []
        self.palabra = ''
        self.guia = ''
        self.lpalabra = 0
        self.puntaje = 0
        self.intentos = 3
        self.alias = ''
        self.dificultad = 0
        self.letrasing = ''

    def carga_dificultad(self, a):
        self.dificultad = int(a)
        return self.dificultad
    
    def devuelve_dificultad(self):
        return self.dificultad
        
    def carga_universo (self):
        print('------------------Cargando Palabra...')
        rand = random.randrange(0, Universo.query.filter(Universo.dificultad==self.dificultad).count())
        qpalabras = Universo.query.filter(Universo.dificultad==self.dificultad)[rand]
        pal = qpalabras.palabra
        print(f'------------------Palabra Cargada: {pal}')
        return pal
    
    #def elegir_palabra(self):
    #    print('------------------Cargando Palabra ')
    #    self.palabra = random.choice(self.palabras)
    #    print('------------------Palabra Cargada ')
    #    return self.palabra

    def cuenta_universo (self):  
        return len(self.palabras)

    def dev_puntaje (self, a):
        if a ==8:
            session["puntaje"] = session["puntaje"] + 15 * session["dificultad"]*2      
        if a ==1 or session["intentos"]==1:
            session["puntaje"] = session["puntaje"] + 2 * session["dificultad"]*2
        elif a ==2 or session["intentos"]==2:
            session["puntaje"] = session["puntaje"] + 4 * session["dificultad"]*2
        elif a ==3 or session["intentos"]==3:
            session["puntaje"] = session["puntaje"] + 6 * session["dificultad"]*2 
        elif a ==4 or session["intentos"]==4:
            session["puntaje"] = session["puntaje"] + 8 * session["dificultad"]*2 
        elif a ==5 or session["intentos"]==5:
            session["puntaje"] = session["puntaje"] + 10 * session["dificultad"]*2
        elif a ==0 or self.intentos==0:
            session["puntaje"] = session["puntaje"]                              
        session["intentos"] = 0
        return session["puntaje"] 

    def largo_palabra(self,a):
        x = len(a)
        return x 
    
    def limpiar_variables_parcial(self):
        self.palabras = []
        self.palabra = ''
        self.guia = ''
        self.lpalabra = 0
        self.intentos = 5
        self.dificultad = 0
        self.letrasing = ''
        session["letrasing"] = ''
        session["intentos"] = 5
        session["guia"] = ''
        session["dificultad"] = None
        session["largo"] = None
    
    def limpiar_variables_total(self):
        self.palabras = []
        self.palabra = ''
        self.guia = ''
        self.lpalabra = 0
        self.puntaje = 0
        self.intentos = 5
        self.alias = ''
        self.dificultad = 0
        self.letrasing = ''

    def getIntentos(self):
        return self.intentos

    def crea_guia(self, ba):
        self.guia = ''
        self.palabra = ba
        self.lpalabra = self.largo_palabra(ba) 
        for x in range(self.lpalabra):
            self.guia = self.guia + '*'  
        return self.guia
    
    def muestra_guia(self,a):
        y = 0
        muestra = ''
        y = len(a)
        for x in range(y):
            muestra = muestra + a[x] 
        return muestra

    def ingresa_letra(self, a):
        print(f'------------------Letra: {a}')
        self.letrasing = self.letrasing  + a + '-'
        session["letrasing"] = session["letrasing"] + a + '-'
        if a in session["palabra"]:
            print('1')
            for i in range(session["largo"]):
                if session["palabra"][i] == a:
                    self.guia = self.guia[:i] + a + self.guia[i+1:]
                    session["guia"] = session["guia"][:i] + a + session["guia"][i+1:]
        else: 
            self.intentos = self.intentos -1
            session["intentos"] = session["intentos"] - 1
        return session["guia"]

    def ingresa_alias(self, a):
        self.alias = a
        return self.alias
        