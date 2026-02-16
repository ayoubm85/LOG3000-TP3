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
    """Multiplie deux nombres.

    Args:
        a (float): Le premier opérande.
        b (float): Le second opérande.

    Returns:
        float: Le produit de a et b.
    """
    return a * b


def divide(a, b):
    """Divise le premier opérande par le second.

    Args:
        a (float): Le dividende.
        b (float): Le diviseur.

    Returns:
        float: Le quotient de a divisé par b.
    """
    return a / b
