"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

"""
Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
import unicodedata

from ADT import list as lt
from DataStructures import listiterator as it

from time import process_time 
from Sorting import insertionsort  as InsSort


def loadCSVFile (file, lst, sep=";")->list:
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep

    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")


    #for i in range (0,len(lst)-1,1):
    #    print (lst[i])
    input ("Ya se cargo el archivo, Clic para continuar")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """

    print("\n**************************************************************************************")
    print("\n Bienvenidos a la consola del RETO 1           ***** EXPLORANDO LAMAGIA DEL CINE *****")
    print("\n**************************************************************************************")
    print ("CARGA DE DATOS")
    print("     (1)  Lab 0 - Cargar Datos de Archivos Large ")
    print("     (2)  Lab 0 - Cargar Datos de Archivos Small ")
    print("     (3)  Lab 0 - Cargar cualquier archivo por nombre")
    print ("")
    print ("REQUERIMIENTO 2 - Crear Ranking de peliculas")
    print("     (4)  Lab 2 - Ordenar por Vote Count Ascendente")
    print("     (5)  Lab 2 - Ordenar por Vote Count Descendente")
    print("     (6)  Lab 2 - Ordenar por Vote Average Ascendente")
    print("     (7)  Lab 2 - Ordenar por Vote Average Descendente")
    print("     (8)  Lab 2 - The Best Movies")
    print("     (9)  Lab 2 - The Worst Movies")
    print("     (10) Lab 2 - Shellsort")
    print("     (11) Lab 2 - Quicksort")

    print ("")
    print ("REQUERIMIENTO 3 - Conocer un director")
    print("     (11) Lab 3 - Listar las peliculas de un director")
    print("     (12) Lab 3 - numero de peliculas del director")
    print("     (13) Lab 3 - promediode la calificacion de las peliculas del director")
    print ("")
    print ("")
    print ("REQUERIMIENTO 5 - Conocer un genero")
    print("     (55) Listar las peliculas de un director")
    print ("")
    print ("REQUERIMIENTO 6 - ranking por genero")
    print("     (66) Listar las peliculas de un director")
    print ("")
    
    print("     0- Salir")

"""   De aqui en adelante  procedimientos para el Lab 0"""
    
def peliculasBuenas(lst1: list)-> int:
    #print(lst1)
    print("Aqui estoy ")
    nRegistros= len(lst1)
    pelBuenas=0
    for i in range (0, nRegistros, 1):
        if (float(lst1[i]['vote_average']) >= 6):
            pelBuenas+=1
            
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")
    return pelBuenas

def PromedioPeliculasBuenas(lst1: list)-> float:
    #print(lst1)
    print("Aqui estoy ")
    nRegistros= len(lst1)
    pelBuenas=0
    proBuenas=0.0
    for i in range (0, nRegistros, 1):
        if (float(lst1[i]['vote_average']) >= 6):
            pelBuenas+=1
            proBuenas= proBuenas + float(lst1[i]['vote_average'])
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")
    proBuenas=proBuenas/pelBuenas
    return proBuenas

def peliculasBuenasDirector(lst1: list, lst2:list,  director:str)-> None:
    #print(lst1)
    print("Aqui estoy ")
    nRegistros= len(lst1)
    pelBuenasDirector=0
    proBuenas=0.0
    NuPeliculas=0
    for i in range (0, nRegistros, 1):
        if ( lst2[i]['director_name'] == director):
            NuPeliculas= NuPeliculas+1
        if (float(lst1[i]['vote_average']) >= 6) and (lst2[i]['director_name'] == director):
            pelBuenasDirector+=1
            proBuenas= proBuenas + float(lst1[i]['vote_average'])
            
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")
    if pelBuenasDirector != 0:
        proBuenas= proBuenas/pelBuenasDirector
        respuesta=(pelBuenasDirector, proBuenas)
    print("El numero de peliculas del director " , director , " son: ", NuPeliculas ,"de las cuales ", pelBuenasDirector, "son buenas. Con un promedio de: ", round(proBuenas,2)) 
    input ("Clic para cotinuar")
#  return respuesta

    """   De aqui en adelante debemos desarrollar los procedimientos para el Lab 1"""


def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0

def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    return 0

def iSort (lst:list, criterio:str, orden:str)->list: 
    t1_start = process_time() #tiempo inicial
    input ("Vamos a proceder a ordenar usando el metodo Insertion Sort, esto puede tomar algunos segundos o minutos. Clic para continuar")
    listaOrdenada = []
    listaOrdenada=InsSort.insertionSort (lst,criterio, orden)
    t1_stop = process_time() #tiempo final
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Tiempo de ejecución de metodo InsertionSort ",t1_stop-t1_start," segundos")
    input ("Dar clic para continuar...")
    return listaOrdenada

def buscarMovies (lista2:list,cantidad:int)->None:
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++  The Best Movies +++++++++++++++++++++++++++++++++")
    for i in range (0,cantidad,1):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(lista2[i],"\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    input ("Dar clic para continuar...")

def buscarMoviesWorst (lista2:list,cantidad:int)->None:
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++  The Best Movies +++++++++++++++++++++++++++++++++")
    for i in range (len(lista2)-1,len(lista2)-12-cantidad,-1):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(lista2[i],"\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    input ("Dar clic para continuar...")







"""
------------------REQUERIMIENTO 5 ------------------------
"""
#input: nombre del genero buscado

#out: lista de todas las peliculas asociadas al genero
#out: cantidad de elementos encontrados
#out: vote count del genero

#metodo para que el input coincida con el formato en caso que no se introduzca una mayuscula, se deja como metodo aparte para reutilización
def normalizeCase(caseInput:str):
    return caseInput.title()
    



def buscarGenero (list1:list, generoBuscado:str):
#definicion variables
    resultList = []
    averageVotes=0
    currentNumVotes=0
    totalVotes=0
#este loop recorre el array importado del csv  y crea un array nuevo con el contenido que cumple el criterio
    for i in range (0, len(list1), 1):
        if (list1[i]['genres'] in normalizeCase(generoBuscado)): #case insensitive
            resultList.append(list1[i])   #se agrega a la lista resultado
            currentNumVotes = int(list1[i]['vote_count'])
            totalVotes= totalVotes + currentNumVotes    
    averageVotes=totalVotes/len(resultList)#calculo del promedio de votos


    print ("Las peliculas encontradas son:" )
    for j in range (len(resultList)):               #loop para imprimir todos los titulos encontrados con un indice
        print((j, resultList[j]['original_title']))
    print ("se encontraron" , len(resultList) , "del genero especificado \nEl promedio de votos para el genero es ", averageVotes)



#req 6 
# input:elegir al menos 10 peliculas
#input:ranking ascendento o descendente
#inputordenar por vote count o  average

#out:lista de peliculas que hacen pare del ranking
#out: vote count y vote average de las peliculas que hace parte del ranking


# def darRankingGenero (lst1:list, genero:str) :

















def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista1 = []  # se require usar lista definida
    lista2 = []  # se require usar lista definida
    lista3 = []   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar:  ') #leer opción ingresada
        print ("Usted selecciono: ", inputs)
        if len(inputs)>0:
            if int(inputs)==1: #opcion 1
                lista1=loadCSVFile("Data/theMoviesdb/AllMoviesDetailsCleaned.csv", lista1) 
                print("Datos cargados de Movies Large, ",len(lista1)," elementos cargados")
                lista2=loadCSVFile("Data/theMoviesdb/AllMoviesCastingRaw.csv", lista2 ) 
                print("Datos cargados de Casting Large, ",len(lista2)," elementos cargados")
                input ("Clic para cotinuar...")

            elif int(inputs)==2: #opcion 2
                lista1=loadCSVFile("Data/theMoviesdb/SmallMoviesDetailsCleaned.csv", lista1) 
                print("Datos cargados de Movies Small, ",len(lista1)," elementos cargados")
                lista2=loadCSVFile("Data/theMoviesdb/MoviesCastingRaw-small.csv", lista2) 
                print("Datos cargados de Casting Small, ",len(lista2)," elementos cargados")
                input ("Clic para cotinuar")
            
            elif int(inputs)==3: #opcion 3
                
                input ("Clic para continuar")
                fileToLoad = input ("Digite el nombre del archivo [ ejemplo: Data/GoodReads/books.csv ] : ")
                lista1=loadCSVFile(fileToLoad) 
                print("Datos cargados del archivo [",fileToLoad, " ]: ", len(lista1))
                
                input ("Clic para cotinuar")

            elif int(inputs)==4: #opcion 4
                orden="less"
                criterio='vote_count'
                #print (lista1)
                #input ("Clic para avanzar")
                lista3=iSort (lista1,criterio, orden)
                print  ("Se ha ordenado la lista")

            elif int(inputs)==5: #opcion 5
                orden="greater"
                criterio='vote_count'
                #print (lista1)
                #input ("Clic para avanzar")
                lista3=iSort (lista1,criterio, orden)
                print  ("Se ha ordenado la lista")
            elif int(inputs)==6: #opcion 6
                orden="less"
                criterio='vote_average'
                #print (lista1)
                #input ("Clic para avanzar")
                lista3=iSort (lista1,criterio, orden)
                print  ("Se ha ordenado la lista")
            elif int(inputs)==7: #opcion 7 
                orden="greater"
                criterio='vote_average'
                #print (lista1)
                #input ("Clic para avanzar")
                lista3=iSort (lista1,criterio, orden)
                print  ("Se ha ordenado la lista")               
                input ("En construccion....Clic para cotinuar")
            elif int(inputs)==8: #opcion 8
                
                cantidad=int(input ("Digite el numero de pelicuales que dea lisar:"))
                buscarMovies (lista1,cantidad)
                input ("En construccion....Clic para cotinuar")

            elif int(inputs)==9: #opcion 9
                cantidad=int(input ("Digite el numero de pelicuales que dea lisar:"))
                buscarMoviesWorst (lista1,cantidad)
                input ("En construccion....Clic para cotinuar")
            elif int(inputs)==10: #opcion 10
                input ("En construccion....Clic para cotinuar")
            elif int(inputs)==11: #opcion 11
                input ("En construccion....Clic para cotinuar")            
            elif int(inputs)==12: #opcion 12
                input ("En construccion....Clic para cotinuar")           
            elif int(inputs)==13: #opcion 13
                input ("En construccion....Clic para cotinuar")     

                

            elif int(inputs)==55: #opcion 10
                cantidad=str(input ("Ingrese el genero a buscar:\n"))
                buscarGenero (lista1,cantidad)
                input ("Clic para cotinuar")

            elif int(inputs)==66: #opcion 10
                pass

            
            elif int(inputs)==0: #opcion 0, salir
                sys.exit(0)  

            
                
if __name__ == "__main__":
    main()