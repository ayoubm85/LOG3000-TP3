"""Tests unitaires pour le module operators.

Ce fichier vérifie le comportement des quatre fonctions arithmétiques
(add, subtract, multiply, divide) définies dans operators.py.
Les tests utilisent des valeurs connues pour détecter d'éventuels bugs
dans l'implémentation des opérations.
"""

import sys
import os
import pytest

# Ajouter le répertoire racine du projet au path pour permettre l'import de operators
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from operators import add, subtract, multiply, divide


# =====================================================================
# Tests de la fonction add
# =====================================================================

class TestAdd:
    """Tests pour la fonction d'addition."""

    def test_add_entiers_positifs(self):
        """Vérifie que l'addition de deux entiers positifs retourne la bonne somme.

        Entrée : a=2, b=3
        Sortie attendue : 5
        """
        assert add(2, 3) == 5

    def test_add_avec_zero(self):
        """Vérifie que l'ajout de zéro ne modifie pas la valeur.

        Entrée : a=7, b=0
        Sortie attendue : 7
        """
        assert add(7, 0) == 7

    def test_add_nombres_negatifs(self):
        """Vérifie l'addition de deux nombres négatifs.

        Entrée : a=-4, b=-6
        Sortie attendue : -10
        """
        assert add(-4, -6) == -10

    def test_add_flottants(self):
        """Vérifie l'addition avec des nombres à virgule flottante.

        Entrée : a=1.5, b=2.5
        Sortie attendue : 4.0
        """
        assert add(1.5, 2.5) == 4.0


# =====================================================================
# Tests de la fonction subtract
# =====================================================================

class TestSubtract:
    """Tests pour la fonction de soustraction.

    La soustraction devrait retourner a - b (premier moins second).
    Un bug potentiel serait une inversion de l'ordre (b - a).
    """

    def test_subtract_entiers_positifs(self):
        """Vérifie que subtract(10, 3) retourne 7 (et non -7).

        Entrée : a=10, b=3
        Sortie attendue : 7
        Bug potentiel : retourne -7 si l'implémentation fait b - a
        """
        assert subtract(10, 3) == 7

    def test_subtract_resultat_negatif(self):
        """Vérifie la soustraction quand le résultat est négatif.

        Entrée : a=3, b=10
        Sortie attendue : -7
        """
        assert subtract(3, 10) == -7

    def test_subtract_avec_zero(self):
        """Vérifie que soustraire zéro ne modifie pas la valeur.

        Entrée : a=5, b=0
        Sortie attendue : 5
        """
        assert subtract(5, 0) == 5

    def test_subtract_nombres_egaux(self):
        """Vérifie que la soustraction de deux nombres égaux donne zéro.

        Entrée : a=8, b=8
        Sortie attendue : 0
        """
        assert subtract(8, 8) == 0


# =====================================================================
# Tests de la fonction multiply
# =====================================================================

class TestMultiply:
    """Tests pour la fonction de multiplication.

    La multiplication devrait retourner a * b.
    Un bug potentiel serait l'utilisation de l'exponentiation (a ** b).
    """

    def test_multiply_entiers_positifs(self):
        """Vérifie que multiply(3, 4) retourne 12 (et non 81).

        Entrée : a=3, b=4
        Sortie attendue : 12
        Bug potentiel : retourne 81 si l'implémentation fait a ** b
        """
        assert multiply(3, 4) == 12

    def test_multiply_par_zero(self):
        """Vérifie que la multiplication par zéro donne zéro.

        Entrée : a=5, b=0
        Sortie attendue : 0
        """
        assert multiply(5, 0) == 0

    def test_multiply_par_un(self):
        """Vérifie que la multiplication par un retourne le même nombre.

        Entrée : a=9, b=1
        Sortie attendue : 9
        """
        assert multiply(9, 1) == 9

    def test_multiply_nombres_negatifs(self):
        """Vérifie la multiplication de deux nombres négatifs.

        Entrée : a=-3, b=-2
        Sortie attendue : 6
        """
        assert multiply(-3, -2) == 6

    def test_multiply_flottants(self):
        """Vérifie la multiplication avec des flottants.

        Entrée : a=2.5, b=4.0
        Sortie attendue : 10.0
        """
        assert multiply(2.5, 4.0) == 10.0


# =====================================================================
# Tests de la fonction divide
# =====================================================================

class TestDivide:
    """Tests pour la fonction de division.

    La division devrait retourner a / b (division flottante).
    Un bug potentiel serait l'utilisation de la division entière (a // b).
    """

    def test_divide_entiers(self):
        """Vérifie que divide(10, 3) retourne ~3.333 (et non 3).

        Entrée : a=10, b=3
        Sortie attendue : 3.333...
        Bug potentiel : retourne 3.0 si l'implémentation fait a // b
        """
        # Utilisation de pytest.approx pour la comparaison de flottants
        assert divide(10, 3) == pytest.approx(10 / 3)

    def test_divide_resultat_entier(self):
        """Vérifie la division quand le résultat est un entier exact.

        Entrée : a=10, b=2
        Sortie attendue : 5.0
        """
        assert divide(10, 2) == 5.0

    def test_divide_par_un(self):
        """Vérifie que la division par un retourne le même nombre.

        Entrée : a=7, b=1
        Sortie attendue : 7.0
        """
        assert divide(7, 1) == 7.0

    def test_divide_flottants(self):
        """Vérifie la division avec des flottants.

        Entrée : a=7.5, b=2.5
        Sortie attendue : 3.0
        """
        assert divide(7.5, 2.5) == 3.0
