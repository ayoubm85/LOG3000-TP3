"""Application web Flask - Calculatrice simple.

Ce module définit une calculatrice web qui accepte des expressions
arithmétiques à un seul opérateur (ex. « 3+5 ») via un formulaire HTML,
les évalue côté serveur et renvoie le résultat à l'utilisateur.

Routes :
    /  (GET)  - Affiche la page de la calculatrice.
    /  (POST) - Évalue l'expression soumise et affiche le résultat.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Table de correspondance entre le caractère opérateur saisi par l'utilisateur
# et la fonction Python associée. Permet un dispatch dynamique dans calculate().
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """Évalue une expression arithmétique simple à un seul opérateur.

    L'expression doit être de la forme « opérande opérateur opérande »
    (ex. « 12+7 » ou « 3.5 * 2 »). Les espaces sont ignorés.

    Args:
        expr (str): L'expression à évaluer (ex. "12+7").

    Returns:
        float: Le résultat numérique de l'opération.

    Raises:
        ValueError: Si l'expression est vide, contient plus d'un
            opérateur, a un format invalide ou des opérandes non numériques.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Retirer tous les espaces pour simplifier le parsing
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Parcourir la chaîne pour localiser l'unique opérateur autorisé
    for i, ch in enumerate(s):
        if ch in OPS:
            # Empêcher les expressions à opérateurs multiples (ex. "3+5-2")
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # L'opérateur ne doit être ni en début ni en fin de chaîne,
    # sinon l'un des opérandes serait manquant
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    # Séparer les deux opérandes de part et d'autre de l'opérateur
    left = s[:op_pos]
    right = s[op_pos+1:]

    # Convertir les opérandes en nombres flottants
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Exécuter l'opération via le dictionnaire de dispatch
    return OPS[op_char](a, b)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Gère la page principale de la calculatrice.

    En GET, affiche la page avec un champ de résultat vide.
    En POST, récupère l'expression saisie dans le formulaire,
    l'évalue via calculate() et affiche le résultat (ou un message
    d'erreur en cas d'expression invalide).

    Returns:
        str: Le rendu HTML du template index.html avec le résultat.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)


# Point d'entrée : lance le serveur de développement Flask
# Le mode debug active le rechargement automatique et les messages d'erreur détaillés
if __name__ == '__main__':
    app.run(debug=True)