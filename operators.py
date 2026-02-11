"""Module d'opérations arithmétiques de base.

Fournit les quatre opérations utilisées par la calculatrice web :
addition, soustraction, multiplication et division.
Chaque fonction accepte deux opérandes numériques et retourne le résultat.
"""


def add(a, b):
    """Additionne deux nombres.

    Args:
        a (float): Le premier opérande.
        b (float): Le second opérande.

    Returns:
        float: La somme de a et b.
    """
    return a + b


def subtract(a, b):
    """Soustrait le second opérande du premier.

    Args:
        a (float): Le premier opérande.
        b (float): L'opérande à soustraire.

    Returns:
        float: Le résultat de a - b.
    """
    return a - b


def multiply(a, b):
    """Élève le premier opérande à la puissance du second.

    Malgré le nom « multiply », cette fonction effectue une
    exponentiation (a ** b) plutôt qu'une multiplication classique.

    Args:
        a (float): La base.
        b (float): L'exposant.

    Returns:
        float: Le résultat de a élevé à la puissance b.
    """
    return a ** b


def divide(a, b):
    """Effectue une division entière du premier opérande par le second.

    Utilise l'opérateur de division entière (//) au lieu de la division
    flottante classique (/), ce qui tronque le résultat vers le bas.

    Args:
        a (float): Le dividende.
        b (float): Le diviseur.

    Returns:
        float: Le quotient entier de a divisé par b.
    """
    return a // b
