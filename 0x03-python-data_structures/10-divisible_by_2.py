#!/usr/bin/python3
""" A function that finds all multiples of 2 in a list """

def divisible_by_2(my_list=[]):
    if my_list:
        lista = []
        for a in my_list:
            if a % 2 == 0:
                lista.append(True)
            else:
                lista.append(False)
        return(lista)
