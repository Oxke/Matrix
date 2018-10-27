#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Classe Matrice"""

__author__ = "Oxke"
__contact__ = "oseaetobia@gmail.com"
__copyright__ = "Copyright (C) 2018, Oxke"

__license__ = "GNU GPLv3.0"  # Read the file LICENSE for more information
__version__ = "v0.3-alpha"
__date__ = "2018-10-25"
__maintainer__ = "Oxke"


class Matrix:
    """Crea ed esegue operazioni tra matrici"""

    def __init__(self, righe):
        if isinstance(righe, str):
            self.righe = tuple(tuple(int(el) for el in riga.strip().split(" "))
                               for riga in righe.split(";"))
        elif isinstance(righe, (list, tuple)):
            self.righe = tuple(righe)
        else:
            raise TypeError("I componenti della matrice devono essere scritti \
o come un iterabile rappresentante le righe o come stringa con righe separate \
da punto e virgola e componenti della righe separati da spazi")
        for i in range(1, len(self.righe)):
            assert len(self.righe[i-1]) == len(self.righe[i]), "Le righe non h\
anno la stessa lunghezza"
        colonne = []
        for i in range(len(self.righe[0])):
            colonne.append((riga[i] for riga in self.righe))
        self.colonne = tuple(colonne)
        self.colonne = tuple(tuple(riga[i] for riga in self.righe) for i in
                             range(len(self.righe[0])))

    def arrotonda(self, cifre=2):
        """arrotonda ogni numero della matrice a due cifre decimali"""
        return Matrix(tuple(tuple(round(el, cifre) for el in riga)
                            for riga in self.righe))

    def __str__(self):
        """formato str, bello, con arrotondamento e parentesi quadre"""
        rnd = self.arrotonda()
        if len(rnd.colonne) == 1:
            stringa = "┎ " + " "*(max([len(str(el[-1]))
                                       for el in rnd.righe])) + " ┒\n"
        else:
            stringa = "┎" + "\t"*(len(rnd.colonne)-1) + " "*(max(
                [len(str(el[-1])) for el in rnd.righe])) + " ┒\n"
        for el_riga in rnd.righe:
            stringa += "┃ " + "\t".join(tuple(str(el) for el in el_riga))
            stringa += " "*(max([len(str(el[-1])) for el in rnd.righe]) -
                            len(str(el_riga[-1])))
            stringa += " ┃\n"
        if len(rnd.colonne) == 1:
            stringa += "┖ " + " "*(max([len(str(el[-1]))
                                        for el in rnd.righe]) + 1) + "┚"
        else:
            stringa += "┖" + "\t"*(len(rnd.colonne) - 1) + " "*(max(
                [len(str(el[-1])) for el in rnd.righe])) + " ┚"
        return stringa

    def __repr__(self):
        return str(self.righe)

    def matr_add(self, oth):
        """Ritorna la somma fra due matrici"""
        assert len(self.righe) == len(oth.righe) and len(self.colonne) == len(
            oth.colonne), "Numero di righe e/o colonne diverso"
        return Matrix(tuple(tuple(self.righe[i][j] + oth.righe[i][j]
                                  for j in range(len(self.colonne)))
                            for i in range(len(self.righe))))

    def __add__(self, *args):
        """ritorna la somma fra piu' addendi matrice"""
        result = self
        for arg in args:
            result = result.matr_add(arg)
        return result

    def opposite(self):
        """returns the opposite of every number in the Matrix"""
        return Matrix(tuple(tuple(-self.righe[i][j]
                                  for j in range(len(self.colonne)))
                            for i in range(len(self.righe))))

    def __sub__(self, b_matr):
        """Sottrae (somma all'opposto)"""
        return self + b_matr.opposite()

    def det(self):
        """ritorna il determinante di una matrice quadrata"""
        assert len(self.righe) == len(self.colonne), "La matrice deve essere q\
uadrata"
        if len(self.righe) == 1:
            return self.righe[0][0]
        somma = 0
        for j in range(len(self.righe[0])):
            somma += self.righe[0][j]*self.compl_alg(1, j+1)
        return somma

    def min_compl(self, r_x, c_y):
        """ritorna il minore complementare di un valore in una matrice"""
        righe = list(self.righe)
        del righe[r_x - 1]
        colonne = [tuple(riga[i] for riga in righe) for i in
                   range(len(righe[0]))]
        del colonne[c_y - 1]
        righe = tuple(tuple(colonna[i] for colonna in colonne) for i in
                      range(len(colonne[0])))
        return Matrix(righe).det()

    def compl_alg(self, r_x, c_y):
        """ritorna il complemento algebrico di un valore in una matrice"""
        return ((-1)**(r_x+c_y))*self.min_compl(r_x, c_y)

    def trasposta(self):
        """Ritorna la matrice trasposta"""
        assert len(self.righe) == len(self.colonne), "La matrice deve essere q\
uadrata"
        m_compl_alg = Matrix(tuple(tuple(self.compl_alg(i, j) for j
                                         in range(1, len(self.colonne) + 1))
                                   for i in range(1, len(self.righe) + 1)))
        return Matrix(m_compl_alg.colonne)

    def inversa(self):
        """Returna la matrice inversa"""
        assert len(self.righe) == len(self.colonne), "La matrice deve essere q\
uadrata"
        return self.trasposta() / self.det()

    @staticmethod
    def uno(lato):
        """Crea matrice UNITA' dato il lato"""
        righe = []
        for i in range(lato):
            riga = []
            for j in range(lato):
                if i == j:
                    riga.append(1)
                else:
                    riga.append(0)
            righe.append(riga)
        return Matrix(righe)

    @staticmethod
    def zero(lato):
        """Crea matrice NULLA dato il lato"""
        return Matrix(tuple(tuple(0 for i in range(lato))
                            for i in range(lato)))

    def matr_mul(self, b_matr):
        """Moltiplicazione fra 2 matrici"""
        if isinstance(b_matr, (int, float)):
            return Matrix(tuple(tuple(el*b_matr for el in riga)
                                for riga in self.righe))
        assert len(self.colonne) == len(b_matr.righe), "Il numero di colonne d\
ella prima matrice deve essere uguale al numero di righe della seconda"
        righe = []
        for s_riga in self.righe:
            riga = []
            for o_colonna in b_matr.colonne:
                result = 0
                for i in range(len(self.colonne)):
                    result += s_riga[i]*o_colonna[i]
                riga.append(result)
            righe.append(tuple(riga))
        return Matrix(righe)

    def __mul__(self, *args):
        """Moltiplicazione fra piu' fattori"""
        result = self
        for arg in args:
            result = result.matr_mul(arg)
        return result

    def __truediv__(self, other):
        """Divide, o meglio moltiplica per l'inverso"""
        if isinstance(other, (int, float)):
            return self * (1/other)
        return self * other.inversa()

    def addrow(self, riga):
        """Aggiunge una riga alla matrice"""
        if isinstance(riga, str):
            self.righe = tuple(list(self.righe) +
                               [tuple(int(el)
                                      for el in riga.strip().split(" "))])
            assert len(self.righe[-1]) == len(self.righe[0]), "Riga di diversa\
 lunghezza rispetto alle altre"
        elif isinstance(riga, (list, tuple)):
            self.righe = tuple(list(self.righe)+[tuple(riga)])
            assert len(self.righe[-1]) == len(self.righe[0]), "Riga di diversa\
 lunghezza rispetto alle altre"
        else:
            raise TypeError("La riga deve essere indicata sotto forma di str\
inga, lista o tuple")
        self.colonne = tuple(tuple(riga[i] for riga in self.righe)
                             for i in range(len(self.righe[0])))

    def addcolumn(self, colonna):
        """Aggiunge una colonna alla matrice"""
        if isinstance(colonna, str):
            self.colonne = tuple(list(self.colonne) +
                                 [tuple(int(el) for el in
                                        colonna.strip().split(" "))])
            assert len(self.colonne[-1]) == len(self.colonne[0]), "Colonna di \
diversa lunghezza rispetto alle altre"
        elif isinstance(colonna, (list, tuple)):
            self.colonne = tuple(list(self.colonne)+[tuple(colonna)])
            assert len(self.colonne[-1]) == len(self.colonne[0]), "Colonna di \
diversa lunghezza rispetto alle altre"
        else:
            raise TypeError("La riga deve essere indicata sotto forma di str\
inga, lista o tuple")
        self.righe = tuple(tuple(colonna[i] for colonna in self.colonne)
                           for i in range(len(self.colonne[0])))
